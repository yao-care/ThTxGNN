/**
 * Drug Lookup - ฟังก์ชันค้นหายา
 * ใช้ Fuse.js สำหรับการค้นหาแบบ Fuzzy รองรับการค้นหาชื่อยาและข้อบ่งใช้
 */
(function() {
  'use strict';

  // Salt suffixes stripped before comparing names (same list as smart-fhir-mapper.js)
  const SALT_SUFFIXES = [
    ' HCL', ' HYDROCHLORIDE', ' SODIUM', ' POTASSIUM',
    ' SULFATE', ' SULPHATE', ' MALEATE', ' ACETATE',
    ' CITRATE', ' PHOSPHATE', ' BROMIDE', ' CHLORIDE',
    ' TARTRATE', ' FUMARATE', ' SUCCINATE', ' MESYLATE',
    ' BESYLATE', ' CALCIUM', ' MAGNESIUM', ' NITRATE',
    ' LACTATE', ' GLUCONATE', ' DISODIUM', ' MONOHYDRATE',
    ' DIHYDRATE', ' TRIHYDRATE', ' ANHYDROUS',
    ' DIPROPIONATE', ' PROPIONATE', ' ACETONIDE',
    ' VALERATE', ' BUTYRATE', ' HEXAHYDRATE',
    ' HBR', ' HYDROBROMIDE', ' MONONITRATE'
  ];

  // Synonym groups (INN / USAN / BAN spellings of the same substance).
  // Order inside a group does not matter: a query is resolved to whichever
  // spelling this site's search-index actually uses (e.g. ASPIRIN ->
  // "Acetylsalicylic Acid" when the index stores that name). Only exact
  // same-substance pairs belong here.
  const SYNONYM_GROUPS = [
    ['ACETYLSALICYLIC ACID', 'ASPIRIN'],
    ['PARACETAMOL', 'ACETAMINOPHEN'],
    ['ADRENALINE', 'EPINEPHRINE'],
    ['NORADRENALINE', 'NOREPINEPHRINE'],
    ['LIGNOCAINE', 'LIDOCAINE'],
    ['FRUSEMIDE', 'FUROSEMIDE'],
    ['SALBUTAMOL', 'ALBUTEROL'],
    ['GLIBENCLAMIDE', 'GLYBURIDE'],
    ['MESALAZINE', 'MESALAMINE'],
    ['CICLOSPORIN', 'CYCLOSPORINE'],
    ['RIFAMPICIN', 'RIFAMPIN'],
    ['ACICLOVIR', 'ACYCLOVIR'],
    ['VALACICLOVIR', 'VALACYCLOVIR'],
    ['CEFALEXIN', 'CEPHALEXIN'],
    ['PETHIDINE', 'MEPERIDINE'],
    ['HYOSCINE', 'SCOPOLAMINE'],
    ['ISOPRENALINE', 'ISOPROTERENOL'],
    ['GLYCERYL TRINITRATE', 'NITROGLYCERIN'],
    ['LEVOTHYROXINE', 'THYROXINE'],
    ['BENZATROPINE', 'BENZTROPINE'],
    ['CLOMIFENE', 'CLOMIPHENE'],
    ['DICYCLOVERINE', 'DICYCLOMINE'],
    ['TRIHEXYPHENIDYL', 'BENZHEXOL'],
    ['ESTRADIOL', 'OESTRADIOL'],
    ['COLECALCIFEROL', 'CHOLECALCIFEROL', 'VITAMIN D3'],
    ['ERGOCALCIFEROL', 'VITAMIN D2'],
    ['PHYTOMENADIONE', 'PHYTONADIONE', 'VITAMIN K1'],
    ['NIACINAMIDE', 'NICOTINAMIDE'],
    ['NICOTINIC ACID', 'NIACIN'],
    ['PYRIDOXINE', 'VITAMIN B6'],
    ['THIAMINE', 'VITAMIN B1'],
    ['RIBOFLAVIN', 'VITAMIN B2'],
    ['CYANOCOBALAMIN', 'VITAMIN B12'],
    ['ASCORBIC ACID', 'VITAMIN C'],
    ['TOCOPHEROL', 'VITAMIN E'],
    ['RETINOL', 'VITAMIN A'],
    ['LEVOMENTHOL', 'L-MENTHOL'],
    ['RACEMENTHOL', 'DL-MENTHOL'],
    ['DEXTROSE', 'GLUCOSE']
  ];

  // Counter-ion words: a name is never reduced to one of these alone
  // (e.g. "POTASSIUM CITRATE" must not become "POTASSIUM").
  const SALT_WORDS = new Set(SALT_SUFFIXES.map(s => s.trim()));

  function stripDiacritics(s) {
    return s.normalize('NFKD').replace(/[̀-ͯ]/g, '');
  }

  // Upper-case, strip accents and parenthetical text, collapse whitespace.
  function baseKey(name) {
    if (!name) return '';
    return stripDiacritics(String(name)).toUpperCase()
      .replace(/\s*\([^)]*\)/g, ' ')
      .replace(/[\s,;]+/g, ' ')
      .trim();
  }

  function stripSalt(key) {
    for (const suffix of SALT_SUFFIXES) {
      if (key.endsWith(suffix)) {
        const rest = key.slice(0, -suffix.length).trim();
        if (rest && !SALT_WORDS.has(rest)) return rest;
        return key;
      }
    }
    return key;
  }

  // Derived lookup keys for a base key: salt-stripped and L-/D-/DL- stripped.
  function derivedKeys(key) {
    const out = [];
    const add = k => { if (k && k !== key && !out.includes(k)) out.push(k); };
    const noSalt = stripSalt(key);
    add(noSalt);
    add(noSalt.replace(/^(DL-|L-|D-)/, ''));
    return out;
  }

  // "AMLODIPINE 5 MG ORAL TABLET" -> "AMLODIPINE"
  function stripDose(key) {
    const tokens = key.split(' ');
    const i = tokens.findIndex(t => /^\d/.test(t));
    return i > 0 ? tokens.slice(0, i).join(' ') : key;
  }

  function synonymsOf(key) {
    const group = SYNONYM_GROUPS.find(g => g.includes(key));
    return group ? group.filter(k => k !== key) : [];
  }


  // Exact lookup tables built from this site's search-index: exact names, then
  // salt/prefix-stripped names, then brand names. A key shared by two different
  // drugs is ambiguous and never used.
  function buildExactIndex(drugs) {
    const idx = { primary: new Map(), derived: new Map(), brand: new Map() };
    const put = (map, key, drug) => {
      if (!key) return;
      if (!map.has(key)) map.set(key, new Set());
      map.get(key).add(drug);
    };
    (drugs || []).forEach(drug => {
      const key = baseKey(drug.name);
      put(idx.primary, key, drug);
      derivedKeys(key).forEach(k => put(idx.derived, k, drug));
      (drug.brands || []).forEach(b => put(idx.brand, baseKey(b), drug));
    });
    return idx;
  }

  function uniqueHit(map, key) {
    const hits = map.get(key);
    return hits && hits.size === 1 ? hits.values().next().value : null;
  }

  // Exact name, salt/prefix-stripped name, synonym (resolved to the spelling this
  // index uses, e.g. aspirin -> Acetylsalicylic Acid), brand name; then the same
  // without dose/form words. No fuzzy step: returns null when unsure.
  function findExactDrug(query) {
    if (!exactIndex) return null;
    const first = baseKey(query);
    const tries = [first];
    const noDose = stripDose(first);
    if (noDose !== first) tries.push(noDose);
    for (const key of tries) {
      const keys = [key].concat(derivedKeys(key));
      for (const map of [exactIndex.primary, exactIndex.derived]) {
        for (const k of keys) { const hit = uniqueHit(map, k); if (hit) return hit; }
      }
      for (const k of keys) {
        for (const s of synonymsOf(k)) {
          for (const map of [exactIndex.primary, exactIndex.derived]) {
            const hit = uniqueHit(map, s); if (hit) return hit;
          }
        }
      }
      const hit = uniqueHit(exactIndex.brand, key);
      if (hit) return hit;
    }
    return null;
  }

  const MATCH_TEXT = {
    "exact": "ชื่อยาตรงกัน",
    "only": "ไม่พบยาที่ชื่อตรงกันทุกตัวอักษร ผลลัพธ์ด้านล่างมีชื่อหรือข้อบ่งใช้เดิมใกล้เคียงกัน ไม่ใช่ยาตัวเดียวกัน โปรดตรวจสอบก่อนเปิด:",
    "after": "ผลลัพธ์ใกล้เคียงอื่น (ไม่ใช่ยาตัวเดียวกัน):",
    "hidden": "{name} ({level}) ชื่อตรงกัน แต่ถูกซ่อนโดยตัวกรองระดับหลักฐาน"
  };

  // รอ DOM และ Fuse.js โหลดเสร็จ
  if (typeof Fuse === 'undefined') {
    console.error('Fuse.js not loaded');
    return;
  }

  const config = window.TWTXGNN_CONFIG || {
    searchIndexUrl: '/data/search-index.json',
    drugsBaseUrl: '/drugs/'
  };

  let searchIndex = null;
  let exactIndex = null;
  let drugFuse = null;
  let indicationFuse = null;

  // องค์ประกอบ DOM
  const input = document.getElementById('lookup-input');
  const searchBtn = document.getElementById('lookup-search');
  const clearBtn = document.getElementById('lookup-clear');
  const results = document.getElementById('lookup-results');
  const levelFilters = document.querySelectorAll('.level-filter');

  if (!input || !results) {
    console.error('Drug lookup elements not found');
    return;
  }

  // โหลดดัชนีค้นหา
  fetch(config.searchIndexUrl)
    .then(r => {
      if (!r.ok) throw new Error('Failed to fetch search index');
      return r.json();
    })
    .then(data => {
      searchIndex = data;
      exactIndex = buildExactIndex(data.drugs);

      // เริ่มต้น Fuse.js
      drugFuse = new Fuse(data.drugs, {
        keys: ['name', 'brands', 'original'],
        threshold: 0.25,
        includeScore: true
      });

      indicationFuse = new Fuse(data.indications, {
        keys: ['name'],
        threshold: 0.25,
        includeScore: true
      });

      console.log('Search index loaded:', data.drug_count, 'drugs,', data.indication_count, 'indications');
    })
    .catch(e => {
      console.error('Failed to load search index:', e);
      results.innerHTML = '<div class="lookup-notice">โหลดดัชนีค้นหาล้มเหลว กรุณารีเฟรชหน้า</div>';
    });

  // ฟังก์ชันอรรถประโยชน์
  function getSelectedLevels() {
    return Array.from(levelFilters)
      .filter(cb => cb.checked)
      .map(cb => cb.value);
  }

  function filterByLevel(items, levels) {
    return items.filter(item => levels.includes(item.level));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // แสดงผลการค้นหา
  function renderResults(query, showHint) {
    if (!searchIndex) {
      results.innerHTML = '<div class="lookup-notice">กำลังโหลดดัชนีค้นหา กรุณารอสักครู่...</div>';
      return;
    }

    if (!query || query.length < 2) {
      if (showHint) {
        results.innerHTML = '<div class="lookup-notice">กรุณาป้อนอย่างน้อย 2 ตัวอักษร</div>';
      } else {
        results.innerHTML = '';
      }
      return;
    }

    const levels = getSelectedLevels();
    if (levels.length === 0 && levelFilters.length > 0) {
      results.innerHTML = '<div class="lookup-notice">กรุณาเลือกระดับหลักฐานอย่างน้อย 1 รายการ</div>';
      return;
    }

    let html = '';

    // ค้นหายา
    // Exact match first; Fuse.js results are only listed as related results and are
    // never shown as the match for the typed name. Levels without a checkbox on
    // this page (e.g. N/A) are not filtered out.
    const filterable = Array.from(levelFilters).map(cb => cb.value);
    const levelOk = lv => !filterable.includes(lv) || levels.includes(lv);
    const exactDrug = findExactDrug(query);
    const exactHidden = exactDrug && !levelOk(exactDrug.level);
    const relatedDrugs = drugFuse.search(query)
      .filter(r => r.item !== exactDrug)
      .map(r => ({ item: r.item, match: 'similar' }));
    const filteredDrugs = (exactDrug ? [{ item: exactDrug, match: 'exact' }] : [])
      .concat(relatedDrugs)
      .filter(r => levelOk(r.item.level))
      .slice(0, 5);

    if (exactHidden) {
      html += '<div class="lookup-notice" data-match="exact-hidden">' +
        MATCH_TEXT.hidden.replace('{name}', escapeHtml(exactDrug.name)).replace('{level}', escapeHtml(exactDrug.level)) + '</div>';
    }

    if (filteredDrugs.length > 0) {
      html += '<div class="result-section"><div class="section-title">ยาที่ตรงกัน</div>';
      let lastMatch = null;
      filteredDrugs.forEach(r => {
        const drug = r.item;
        const brands = drug.brands && drug.brands.length > 0
          ? ' (' + drug.brands.slice(0, 2).join('、') + ')'
          : '';
        const filteredInds = filterByLevel(drug.indications || [], levels);

        if (r.match !== lastMatch) {
          const note = r.match === 'exact' ? MATCH_TEXT.exact : (exactDrug ? MATCH_TEXT.after : MATCH_TEXT.only);
          html += '<div class="match-note match-' + r.match + '" style="font-size:0.85em;color:#555;margin:0.5rem 0 0.25rem;">' + escapeHtml(note) + '</div>';
          lastMatch = r.match;
        }
        html += '<div class="result-card" data-match="' + r.match + '">';
        html += '<div class="result-header">';
        html += '<a href="' + (drug.url || config.drugsBaseUrl + drug.slug + '/') + '" class="drug-name">' + escapeHtml(drug.name) + escapeHtml(brands) + '</a>';
        html += '<span class="level-badge level-' + drug.level + '">' + drug.level + '</span>';
        html += '</div>';
        html += '<div class="result-original">ข้อบ่งใช้เดิม: ' + (escapeHtml(drug.original) || '—') + '</div>';
        html += '<div class="result-indications"><strong>ข้อบ่งใช้ใหม่ที่ทำนาย:</strong>';

        if (filteredInds.length > 0) {
          filteredInds.slice(0, 5).forEach(ind => {
            html += '<span class="ind-item"><span class="level-badge level-' + ind.level + '">' + ind.level + '</span> ' + escapeHtml(ind.name) + ' (' + ind.score + '%)</span>';
          });
          if (filteredInds.length > 5) {
            html += '<span class="more">...อีก ' + filteredInds.length + ' รายการ</span>';
          }
        } else {
          html += '<span class="no-match">(ไม่ตรงกับเกณฑ์การกรอง)</span>';
        }

        html += '</div>';
        html += '<a href="' + (drug.url || config.drugsBaseUrl + drug.slug + '/') + '" class="view-report">ดูรายงานฉบับเต็ม →</a>';
        html += '</div>';
      });
      html += '</div>';
    }

    // ค้นหาข้อบ่งใช้
    const indResults = indicationFuse.search(query).slice(0, 5);
    const filteredInds = indResults.filter(r => levels.includes(r.item.level));

    if (filteredInds.length > 0) {
      html += '<div class="result-section"><div class="section-title">ข้อบ่งใช้ที่ตรงกัน</div>';
      filteredInds.forEach(r => {
        const ind = r.item;
        const indDrugs = filterByLevel(ind.drugs || [], levels);

        html += '<div class="result-card">';
        html += '<div class="result-header">';
        html += '<span class="indication-name">' + escapeHtml(ind.name) + '</span>';
        html += '<span class="level-badge level-' + ind.level + '">' + ind.level + '</span>';
        html += '</div>';
        html += '<div class="result-drugs"><strong>ยาที่อาจได้ผล (' + indDrugs.length + ' รายการ):</strong>';

        indDrugs.slice(0, 5).forEach(d => {
          html += '<div class="drug-item">';
          html += '<a href="' + (d.url || config.drugsBaseUrl + d.slug + '/') + '">' + escapeHtml(d.name) + '</a>';
          html += '<span class="level-badge level-' + d.level + '">' + d.level + '</span>';
          html += '<span class="score">' + d.score + '%</span>';
          html += '<span class="original-hint">' + escapeHtml(d.original) + '</span>';
          html += '</div>';
        });

        if (indDrugs.length > 5) {
          html += '<div class="more">...อีก ' + indDrugs.length + ' ยา</div>';
        }

        html += '</div></div>';
      });
      html += '</div>';
    }

    if (!html) {
      html = '<div class="lookup-notice">ไม่พบผลลัพธ์ที่ตรงกับเกณฑ์</div>';
    }

    results.innerHTML = html;
  }

  // ดำเนินการค้นหา
  function doSearch() {
    renderResults(input.value.trim(), true);
  }

  // ฟังเหตุการณ์
  let debounceTimer;

  input.addEventListener('input', function() {
    if (clearBtn) {
      clearBtn.style.display = this.value ? 'block' : 'none';
    }
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function() {
      renderResults(input.value.trim(), false);
    }, 300);
  });

  input.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      doSearch();
    }
  });

  if (searchBtn) {
    searchBtn.addEventListener('click', doSearch);
  }

  if (clearBtn) {
    clearBtn.addEventListener('click', function() {
      input.value = '';
      clearBtn.style.display = 'none';
      results.innerHTML = '';
      input.focus();
    });
  }

  levelFilters.forEach(function(cb) {
    cb.addEventListener('change', function() {
      renderResults(input.value.trim(), false);
    });
  });

})();

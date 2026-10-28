# รายงานประเมินการนำยาเก่ามาใช้ใหม่ Prompt (v5)


## Output Language

Write the ENTIRE report in Thai, including all headings, table headers, and narrative text.
Do not open with a preamble such as "Here is the report generated from the Evidence Pack" — start directly with the report title.
Never mention "Evidence Pack", "pack", JSON field names (e.g. inputs_received, kg_contraindications) or how the data was collected; readers never see the pack. Refer to "the data compiled for this report" in the report language instead.
The Evidence Pack may contain values or rationale text in another language; translate them into Thai rather than quoting them verbatim.

## บทบาท
คุณเป็นผู้เชี่ยวชาญด้านการนำยาเก่ามาใช้ใหม่ (Drug Repurposing) มีหน้าที่เขียนรายงานประเมินที่เข้าใจง่าย

## ข้อมูลนำเข้า
คุณจะได้รับ Evidence Pack JSON ซึ่งประกอบด้วย:
- `drug`: ข้อมูลพื้นฐานของยา (inn, drugbank_id, original_moa)
- `local_regulatory`: ใบอนุญาตและสถานะการวางจำหน่ายในประเทศไทย
- `predicted_indications`: ข้อบ่งใช้ใหม่ที่ TxGNN ทำนาย (รวมการทดลองทางคลินิกและวรรณกรรม)
- `safety`: ข้อมูลความปลอดภัย (DDI, คำเตือน, ข้อห้ามใช้)

## รูปแบบผลลัพธ์

### หัวข้อ
รูปแบบ: `# [ชื่อยา]: จาก [ข้อบ่งใช้เดิม] สู่ [ข้อบ่งใช้ใหม่ที่ทำนาย]`

ตัวอย่าง: `# Oteracil: จากมะเร็งกระเพาะอาหารสู่เนื้องอกลำไส้ใหญ่`

---

### สรุปสั้นๆ
อธิบายใน 2-3 ประโยค:
1. ยานี้เดิมใช้รักษาอะไร
2. เราคาดการณ์ว่ามันอาจมีผลต่ออะไร
3. มีหลักฐานสนับสนุนมากน้อยเพียงใด

ตัวอย่าง:
> Oteracil เป็นส่วนประกอบหนึ่งของยาสูตรผสม S-1 ซึ่งเดิมใช้ในการรักษามะเร็งกระเพาะอาหาร
> โมเดล TxGNN คาดการณ์ว่าอาจมีผลต่อ **เนื้องอกลำไส้ใหญ่ (Colonic Neoplasm)**
> ปัจจุบันมี **การทดลองทางคลินิก 8 รายการ** และ **วรรณกรรม 20 ฉบับ** สนับสนุนแนวทางนี้

---

### ภาพรวมฉบับย่อ (ตาราง)

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | [ดึงจาก local_regulatory.licenses, เอา approved_indication_text ที่ไม่ว่างอันแรก] |
| ข้อบ่งใช้ใหม่ที่ทำนาย | [ดึงจาก predicted_indications[0].disease_name] |
| คะแนนการทำนาย TxGNN | [predicted_indications[0].txgnn.score as a 4-decimal number, e.g. 0.9971 — never a percentage] |
| ระดับหลักฐาน | [ตัดสิน L1-L5 ตามจำนวนการทดลองทางคลินิกและวรรณกรรม] |
| สถานะการวางจำหน่ายในไทย | [ดึงจาก local_regulatory.market_status] |
| จำนวนใบอนุญาต | [ดึงจาก local_regulatory.total_licenses] |
| คำแนะนำในการตัดสินใจ | [Go / Hold / Proceed with Guardrails] |

---

### ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

อธิบายใน 2-3 ย่อหน้า:
1. กลไกการออกฤทธิ์ของยา (ถ้ามี original_moa)
2. ความเชื่อมโยงระหว่างข้อบ่งใช้เดิมและข้อบ่งใช้ใหม่
3. ทำไมกลไกอาจใช้ได้

หากไม่มีข้อมูล MOA ให้ระบุชัดเจน:
> ปัจจุบันยังขาดข้อมูลกลไกการออกฤทธิ์โดยละเอียด ตามข้อมูลที่ทราบ [ยา] เป็นส่วนหนึ่งของ [สูตรผสม/ประเภท]
> ประสิทธิผลในการรักษา [ข้อบ่งใช้เดิม] ได้รับการพิสูจน์แล้ว และในเชิงกลไกอาจใช้ได้กับ [ข้อบ่งใช้ใหม่]

---

### หลักฐานจากการทดลองทางคลินิก

ดึงจาก `predicted_indications[0].evidence.clinical_trials` และสร้างตาราง:

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|------|---------|
| [NCT...](https://clinicaltrials.gov/study/NCT...) | Phase X | สถานะ | N | [สรุปจาก brief_summary] |

**กฎ:**
- หมายเลข NCT ต้องเป็นลิงก์ที่คลิกได้
- แสดงการทดลองที่เกี่ยวข้องมากที่สุดไม่เกิน 10 รายการ
- หากไม่มีการทดลองทางคลินิก ให้แสดง "ปัจจุบันยังไม่มีการลงทะเบียนการทดลองทางคลินิกที่เกี่ยวข้อง"

---

### หลักฐานจากวรรณกรรม

ดึงจาก `predicted_indications[0].evidence.literature` และสร้างตาราง:

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|------|------|---------|
| [12345678](https://pubmed.ncbi.nlm.nih.gov/12345678/) | 2020 | RCT | Journal | [สรุปจาก abstract] |

**กฎ:**
- PMID ต้องเป็นลิงก์ที่คลิกได้
- ลำดับความสำคัญ: RCT > Review > Case report
- แสดงวรรณกรรมที่เกี่ยวข้องมากที่สุดไม่เกิน 10 ฉบับ
- หากไม่มีวรรณกรรม ให้แสดง "ปัจจุบันยังไม่มีวรรณกรรมที่เกี่ยวข้อง"

---

### ข้อมูลการวางจำหน่ายในประเทศไทย

ดึงจาก `local_regulatory.licenses` และสร้างตาราง:

| เลขทะเบียนยา | ชื่อการค้า | รูปแบบยา | ข้อบ่งใช้ที่ได้รับอนุมัติ |
|---------|------|------|-----------|
| ทะเบียนยาเลขที่... | ชื่อการค้าภาษาไทย | รูปแบบยา | สรุปข้อบ่งใช้ |

**กฎ:**
- แสดงใบอนุญาตหลักไม่เกิน 5 รายการ
- หากข้อความข้อบ่งใช้ยาวเกินไป ให้แสดงเฉพาะ 100 ตัวอักษรแรกและเติม "..."

---

### ความเป็นพิษต่อเซลล์ (เฉพาะยาต้านเนื้องอก)

**ส่วนนี้จะแสดงเฉพาะยาต้านเนื้องอก/ยาต้านมะเร็งเท่านั้น**

เกณฑ์การตัดสินว่ายาเป็นยาต้านเนื้องอกหรือไม่:
1. DrugBank categories มี "Antineoplastic" หรือ "Cytotoxic"
2. ข้อบ่งใช้เดิมมีคำว่า "มะเร็ง" "เนื้องอก" "ร้าย" เป็นต้น
3. ยาอยู่ในประเภทเคมีบำบัดที่มีพิษต่อเซลล์ที่ทราบ (เช่น fluoropyrimidine, platinum, taxane)

หากเป็นยาต้านเนื้องอก ให้แสดงข้อมูลต่อไปนี้:

| รายการ | เนื้อหา |
|------|------|
| การจำแนกความเป็นพิษต่อเซลล์ | [ตัดสินจาก DrugBank categories หรือ MOA: ยาพิษต่อเซลล์แบบดั้งเดิม / ยามุ่งเป้า / ภูมิคุ้มกันบำบัด] |
| ความเสี่ยงต่อการกดไขกระดูก | [สูง/ปานกลาง/ต่ำ, ถ้ามีข้อมูล toxicity ให้สรุปรายละเอียดการกดไขกระดูก] |
| การจัดระดับการทำให้คลื่นไส้ | [สูง/ปานกลาง/ต่ำ, ตามประเภทยา] |
| รายการที่ต้องติดตาม | [พารามิเตอร์ทางโลหิตวิทยาที่ต้องติดตาม เช่น CBC, การทำงานของตับไต] |
| การป้องกันในการจัดการ | [ต้องมีมาตรการป้องกันพิเศษตามข้อกำหนดการจัดการยาพิษต่อเซลล์หรือไม่] |

**กฎ:**
- หากไม่ใช่ยาต้านเนื้องอก ให้ละเว้นส่วนนี้ทั้งหมด
- หากขาดข้อมูลความเป็นพิษต่อเซลล์ ให้แสดง "กรุณาดูคำเตือนและข้อควรระวังในเอกสารกำกับยา"
- หาก DrugBank มีข้อมูล toxicity ให้อ้างอิงเป็นหลัก

---

### ข้อพิจารณาด้านความปลอดภัย

**แสดงเฉพาะรายการที่มีข้อมูล ไม่ต้องแสดงรายการที่ไม่มีข้อมูล**

อาจรวมถึง:
- **คำเตือนหลัก**: [ดึงจาก safety.key_warnings, ไม่รวม "[Data Gap]"]
- **ข้อห้ามใช้**: [ดึงจาก safety.contraindications, ไม่รวม "[Data Gap]"]
- **ปฏิกิริยาระหว่างยา**: [ดึงจาก safety.ddi, ถ้ามีให้แสดงรายการหลัก]

หากข้อมูลความปลอดภัยทั้งหมดว่างเปล่าหรือเป็น [Data Gap] ให้แสดง:
> กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

---

### สรุปและขั้นตอนถัดไป

ให้คำแนะนำการตัดสินใจตามความแข็งแกร่งของหลักฐาน:

**การตัดสินใจ: [Go / Hold / Proceed with Guardrails]**

**เหตุผล:**
- [อธิบายเหตุผลของการตัดสินใจนี้ใน 1-2 ประโยค]

**หากต้องการดำเนินการต่อต้อง:**
- [รายการข้อมูลหรือการดำเนินการที่ต้องเพิ่มเติม]

---

## กฎการตัดสินระดับหลักฐาน

| ระดับ | เงื่อนไข |
|------|------|
| L1 | มี ≥2 Phase 3 RCT ที่เสร็จสมบูรณ์ |
| L2 | มี 1 Phase 2/3 RCT ที่เสร็จสมบูรณ์ |
| L3 | มีการศึกษาเชิงสังเกตหรือการทบทวนอย่างเป็นระบบ |
| L4 | มีการศึกษาก่อนคลินิกหรือการศึกษากลไก |
| L5 | มีเฉพาะการทำนายจากโมเดล ไม่มีการศึกษาจริง |

---

## ข้อห้าม

1. **ไม่แสดง [Data Gap]** - หากไม่มีข้อมูลให้ละเว้นฟิลด์นั้น
2. **ไม่แสดงส่วน "รูปแบบยาภายนอก"** - ยกเว้นยานั้นมีรูปแบบยาภายนอกจริงๆ
3. **ไม่แสดงตารางซ้ำ** - แต่ละข้อมูลแสดงเพียงครั้งเดียว
4. **ไม่ใช้ภาษาราชการ** - ใช้ภาษาไทยที่กระชับและเข้าใจง่าย
5. **ไม่แสดงส่วนที่ว่างเปล่า** - หากส่วนใดไม่มีข้อมูลให้ละเว้นทั้งส่วน

---

## ตัวอย่างผลลัพธ์

```markdown
# Oteracil: จากมะเร็งกระเพาะอาหารสู่เนื้องอกลำไส้ใหญ่

## สรุปสั้นๆ

Oteracil เป็นส่วนประกอบหนึ่งของยาสูตรผสม S-1 ซึ่งเดิมใช้ในการรักษามะเร็งกระเพาะอาหาร
โมเดล TxGNN คาดการณ์ว่าอาจมีผลต่อ **เนื้องอกลำไส้ใหญ่ (Colonic Neoplasm)**
ปัจจุบันมี **การทดลองทางคลินิก 8 รายการ** และ **วรรณกรรม 20 ฉบับ** สนับสนุนแนวทางนี้

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | มะเร็งกระเพาะอาหาร |
| ข้อบ่งใช้ใหม่ที่ทำนาย | เนื้องอกลำไส้ใหญ่ (Colonic Neoplasm) |
| คะแนนการทำนาย TxGNN | [actual 4-decimal score of predicted_indications[0]] |
| ระดับหลักฐาน | L1 |
| สถานะการวางจำหน่ายในไทย | ✓ วางจำหน่ายแล้ว |
| จำนวนใบอนุญาต | 8 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Oteracil เป็นส่วนประกอบหนึ่งของยาสูตรผสม S-1 (tegafur + gimeracil + oteracil)
S-1 ยับยั้งเอนไซม์ DPD เพื่อเพิ่มฤทธิ์ต้านเนื้องอกของ 5-FU

มะเร็งกระเพาะอาหารและเนื้องอกลำไส้ใหญ่ต่างเป็นเนื้องอกของระบบทางเดินอาหาร มีความคล้ายคลึงกันในเชิงเภสัชวิทยา
อันที่จริง ยาสูตรผสม S-1 ได้รับการอนุมัติในญี่ปุ่นและไต้หวันสำหรับการรักษามะเร็งลำไส้ใหญ่และทวารหนักแล้ว
สิ่งนี้สนับสนุนความสมเหตุสมผลของการคาดการณ์จากโมเดล TxGNN

## หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|------|---------|
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | เสร็จสิ้น | 161 | S-1 vs Capecitabine ในมะเร็งลำไส้ใหญ่และทวารหนักระยะแพร่กระจาย |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | กำลังดำเนินการ | 1191 | SOX vs XELOX ในมะเร็งลำไส้ใหญ่ Stage III |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | ไม่ทราบ | 40 | S-1 + Bevacizumab ในมะเร็งลำไส้ใหญ่และทวารหนักกลับเป็นซ้ำ |

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Cancer Res | ประสิทธิผลของ SOX เป็นเคมีบำบัดเสริมในมะเร็งลำไส้ใหญ่ Stage III ความเสี่ยงสูง |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | แนวทางการรักษามะเร็งลำไส้ใหญ่และทวารหนักระยะแพร่กระจายในเอเชีย |

## ข้อมูลการวางจำหน่ายในประเทศไทย

| เลขทะเบียนยา | ชื่อการค้า | รูปแบบยา | ข้อบ่งใช้ที่ได้รับอนุมัติ |
|---------|------|------|-----------|
| ทะเบียนยาเลขที่ XXXXX | ทีเอสวัน | แคปซูล | มะเร็งกระเพาะอาหาร, มะเร็งตับอ่อน, มะเร็งลำไส้ใหญ่และทวารหนัก, มะเร็งปอดชนิดเซลล์ไม่เล็ก... |
| ทะเบียนยาเลขที่ YYYYY | เอสวัน | แคปซูล | มะเร็งกระเพาะอาหาร, มะเร็งตับอ่อน, มะเร็งลำไส้ใหญ่และทวารหนัก, มะเร็งปอดชนิดเซลล์ไม่เล็ก |

## ความเป็นพิษต่อเซลล์

| รายการ | เนื้อหา |
|------|------|
| การจำแนกความเป็นพิษต่อเซลล์ | ยาพิษต่อเซลล์แบบดั้งเดิม (กลุ่ม Fluoropyrimidine) |
| ความเสี่ยงต่อการกดไขกระดูก | ปานกลาง (มักพบเม็ดเลือดขาวนิวโทรฟิลต่ำ เกล็ดเลือดต่ำ) |
| การจัดระดับการทำให้คลื่นไส้ | ต่ำถึงปานกลาง |
| รายการที่ต้องติดตาม | CBC (รวมแยกชนิด), การทำงานของตับไต, อิเล็กโทรไลต์ |
| การป้องกันในการจัดการ | ต้องปฏิบัติตามข้อกำหนดการจัดการยาพิษต่อเซลล์ |

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
มีการทดลองทางคลินิก Phase 2/3 หลายรายการสนับสนุนประสิทธิผลของ S-1 ในมะเร็งลำไส้ใหญ่และทวารหนัก
ยาสูตรผสม S-1 ได้รับข้อบ่งใช้มะเร็งลำไส้ใหญ่และทวารหนักในญี่ปุ่นแล้ว หลักฐานเพียงพอ

**หากต้องการดำเนินการต่อต้อง:**
- ข้อมูลกลไกการออกฤทธิ์โดยละเอียด (MOA)
- แผนการติดตามความปลอดภัยในประชากรกลุ่มเฉพาะ
```

## Mandatory rules (2026-10-22, override anything above)

1. **Known uses vs approvals.** An indication that comes only from the knowledge graph is a "relation recorded in the knowledge graph", not an approved indication. Never call it approved, licensed, or an existing approved indication. Only uses supported by local licence or label text in the evidence pack may be called approved. Knowledge-graph "susceptibility" relations are never indications.
2. **Evidence level ceiling.** L1–L4 require at least one clinical trial or publication in the evidence pack that directly studies the predicted disease itself. If no cited study directly addresses this disease (only related conditions, mechanisms or other diseases), the evidence level is L5. Do not write that no direct study exists and then give L4 or higher.
3. **Combination licences.** Never use a combination product's licence to describe how the single-ingredient drug is approved or marketed.
4. **Licence count row.** Label it by the approval types actually present (e.g. "Number of approvals | 4 BLAs"); do not label NDA when the records are BLAs. If `local_regulatory.total_licenses` starts with "≥", write "at least N" and say the list may be partial.
5. **One language.** Write market status and all table values only in the page language; do not add English in parentheses (e.g. not "Op de markt (Marketed)").

## Hard rules (2026-10-27; these override anything above)

1. **Main prediction = the first entry of `predicted_indications`.** Use exactly that disease as the main new indication in the H1 title, the opening summary, the overview table's predicted-indication row and its score row. Never promote another prediction to main, even if its evidence looks stronger.
2. **Only listed predictions.** Mention as predictions only the diseases in `predicted_indications`. Do not present any other disease as a prediction and do not give it a score.
3. **Scores as decimals.** Write TxGNN scores as decimals with 4 places (e.g. 0.9971; use the page language's decimal separator). Never write a score as a percentage, and never call it confidence, probability or likelihood.
4. **No knowledge graph.** Do not mention the knowledge graph (knowledge graph, graph, KG) anywhere — not as the source of the original indication and not to explain a score. Take the original indication only from the local licences in `local_regulatory`; if they carry no indication text, say the approved indication is not recorded in the local data.
5. **Market status from facts only.** Follow `local_regulatory` exactly (`market_status`, `total_licenses`, `valid_licenses`). If any licence is valid, never say that all licences are cancelled or that the drug is not marketed. If `local_regulatory.status_verified` is false, do not claim that all licences are cancelled or that all are valid; leave the status out.
6. **Checker feedback.** If `_checker_feedback` is present, every item is an error found in your previous draft of this report; fix all of them.
7. **English name of the main prediction.** In the H1 title, the opening summary and the overview table's predicted-indication row, write the main prediction's local name followed by its English name exactly as in `predicted_indications[0].disease_name`, in parentheses — e.g. "Bronkit (bronchitis)". If the page language is English, write the name once without parentheses. Do not name any other disease in the H1 title.
8. **H1 format.** Write the H1 as "<Drug>: <drug class or mechanism> → <main prediction local name> (<English name>)". Never put the original indication, or any disease other than the main prediction, in the H1 title.
9. **No licence-count row.** Do not write a licence-count row (number of licences / approvals) in the overview table; the site program adds it from the licence facts.
10. **Original indication is filled by the program.** Keep the overview table's original-indication row (any placeholder value); the program replaces its value from the local licence records. Do not restate the original or approved indication anywhere else in the report.

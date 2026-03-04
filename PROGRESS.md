# ThTxGNN 開發進度記錄

> 最後更新：2026-03-04

## 專案概述

ThTxGNN 是泰國版藥品老藥新用預測系統，基於 TwTxGNN（台灣版）改編。

## 已完成工作

### Phase 1-4：基礎建設 ✅
- [x] 專案初始化與重新命名
- [x] ThaiFDA 資料整合
- [x] 疾病映射（泰文→英文）
- [x] KG 預測流程
- [x] 網站與 FHIR 基礎設施
- [x] 所有頁面翻譯為泰文

### Phase 5：證據收集流程 ✅
- [x] `src/thtxgnn/collectors/drug_bundle.py` - DrugBundle 聚合器
- [x] `scripts/batch_collect_bundles.py` - 批量收集 Bundle
- [x] `scripts/batch_generate_reports.py` - 批量生成報告（需 OPENAI_API_KEY）
- [x] `prompts/` - LLM 提示詞目錄

### Phase 6：文件同步流程 ✅
- [x] `scripts/sync_notes_to_docs.py` - 同步藥師筆記到 Jekyll
- [x] `scripts/generate_search_index.py` - 生成搜索索引

## 目前狀態

### 已收集的藥品 Bundle（6 個）

| 藥品 | 適應症 | 臨床試驗 | PubMed | 證據等級 |
|------|--------|----------|--------|----------|
| Amlodipine | 3 | 0 | 20 | L4 |
| Allopurinol | 10 | 0 | 9 | L4 |
| Isosorbide dinitrate | 10 | 49 | 40 | L1 |
| Lidocaine | 10 | 19 | 29 | L3 |
| Nystatin | 10 | 2 | 40 | L3 |
| Prednisolone | 10 | 26 | 51 | L1 |
| **總計** | **53** | **96** | **189** | - |

### 目錄結構

```
ThTxGNN/
├── data/
│   ├── bundles/           # 已收集的藥品 Bundle（6 個）
│   ├── collected/         # 原始收集資料
│   │   ├── clinicaltrials/
│   │   ├── drugbank/
│   │   ├── pubmed/
│   │   ├── tctr/          # 泰國臨床試驗註冊
│   │   └── thaifda/
│   ├── evidence_packs/    # LLM 分析結果（尚未生成）
│   └── notes/             # 藥師筆記（尚未生成）
├── prompts/               # LLM 提示詞
│   ├── Evidence Pack Reviewer/
│   ├── Notes Writer/
│   └── Modules/
├── scripts/
│   ├── batch_collect_bundles.py
│   ├── batch_generate_reports.py
│   ├── sync_notes_to_docs.py
│   └── generate_search_index.py
└── docs/
    ├── _drugs/            # 藥品頁面（151 個現有頁面）
    └── data/
        └── search-index.json
```

## 下一步工作

### 選項 A：生成 LLM 報告（需要 OPENAI_API_KEY）

```bash
cd /Users/lightman/yao.care/ThTxGNN

# 設定 API Key
export OPENAI_API_KEY='your-key-here'

# 為已收集的 Bundle 生成報告
uv run python scripts/batch_generate_reports.py --all

# 同步到文件網站
uv run python scripts/sync_notes_to_docs.py

# 更新搜索索引
uv run python scripts/generate_search_index.py

# 更新 FHIR 資源
uv run python scripts/generate_fhir_resources.py
```

### 選項 B：收集更多藥品 Bundle（不需要 API Key）

```bash
cd /Users/lightman/yao.care/ThTxGNN

# 收集更多藥品（例如前 50 個）
uv run python scripts/batch_collect_bundles.py --limit 50 --skip-existing

# 或指定特定藥品
uv run python scripts/batch_collect_bundles.py --drugs "Metformin,Aspirin,Omeprazole"
```

## 完整工作流程圖

```
┌─────────────────────────────────────────────────────────────┐
│  1. 收集 Bundle（無需 API Key）                              │
│     python scripts/batch_collect_bundles.py --limit N       │
│     → data/bundles/{drug}/drug_bundle.json                  │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  2. 生成報告（需要 OPENAI_API_KEY）                          │
│     python scripts/batch_generate_reports.py --all          │
│     → data/evidence_packs/{drug}/                           │
│     → data/notes/{drug}/drug_pharmacist_notes.md            │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  3. 同步到 Jekyll                                            │
│     python scripts/sync_notes_to_docs.py                    │
│     → docs/_drugs/{drug}.md                                 │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  4. 更新索引與 FHIR                                          │
│     python scripts/generate_search_index.py                 │
│     python scripts/generate_fhir_resources.py               │
│     → docs/data/search-index.json                           │
│     → docs/fhir/*                                           │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  5. 部署                                                     │
│     git add . && git commit && git push                     │
│     → GitHub Pages 自動部署                                  │
└─────────────────────────────────────────────────────────────┘
```

## Git 提交歷史

```
e9e4046 Add workflow scripts and sample drug bundles
d6c0c8d Add LLM prompts for evidence pack and notes generation
9e48d30 Add evidence collection and report generation from TwTxGNN
d970d9d Fix Thai news fetching and require both drug+disease in news
```

## 相關文件

- `CLAUDE.md` - 國際化 SOP 與開發指南
- `README.md` - 專案說明
- `pyproject.toml` - Python 專案設定

---

*此文件由 Claude Code 自動生成*

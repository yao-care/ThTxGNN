---
layout: default
title: SMART on FHIR
nav_order: 2
has_children: true
description: ThTxGNN SMART on FHIR 應用程式 - 從 EHR 讀取用藥並查詢老藥新用候選
permalink: /smart/
---

# SMART on FHIR 應用程式

ThTxGNN 提供 SMART on FHIR 整合，讓醫療機構可以從電子病歷系統（EHR）讀取病患用藥資料，自動查詢相關的老藥新用候選。

---

## 什麼是 SMART on FHIR？

SMART on FHIR 是一個開放標準，讓醫療應用程式可以安全地存取電子病歷系統中的資料。透過這個標準：

- 應用程式可以從 EHR 系統獲取授權
- 讀取病患的用藥記錄、診斷等資料
- 在 EHR 工作流程中無縫整合

---

## 功能特色

| 功能 | 說明 |
|------|------|
| **病患用藥讀取** | 自動從 EHR 獲取病患目前的用藥清單 |
| **藥物映射** | 將 RxNorm 藥物代碼映射到 ThTxGNN 資料庫 |
| **老藥新用查詢** | 顯示每個藥物的預測新適應症候選 |
| **證據等級標示** | 清楚標示每個預測的證據等級（L1-L5） |
| **臨床試驗查詢** | 即時查詢 ClinicalTrials.gov 相關臨床試驗 |
| **藥物交互作用** | 自動檢查 DDI 並顯示警示 |

---

## 快速開始

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); border-radius: 12px; border: 2px solid #4caf50;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
    <strong style="font-size: 1.1rem; color: #2e7d32;">獨立測試模式</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">不需要 EHR 連線，直接輸入藥物名稱測試功能</p>
    <a href="standalone.html" style="display: inline-block; padding: 8px 16px; background: #4caf50; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">立即體驗 →</a>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); border-radius: 12px; border: 2px solid #2196f3;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📖</div>
    <strong style="font-size: 1.1rem; color: #1565c0;">使用指南</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">圖文教學：如何使用 ThTxGNN SMART App</p>
    <a href="guide/" style="display: inline-block; padding: 8px 16px; background: #2196f3; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">查看指南 →</a>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); border-radius: 12px; border: 2px solid #ff9800;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚙️</div>
    <strong style="font-size: 1.1rem; color: #e65100;">技術文件</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">OAuth 配置、FHIR API、藥物映射流程</p>
    <a href="technical-docs/" style="display: inline-block; padding: 8px 16px; background: #ff9800; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">技術規格 →</a>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); border-radius: 12px; border: 2px solid #9c27b0;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔗</div>
    <strong style="font-size: 1.1rem; color: #7b1fa2;">整合資源</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">ClinicalTrials.gov、DDI 檢查、CDS Hooks</p>
    <a href="integrations/" style="display: inline-block; padding: 8px 16px; background: #9c27b0; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">查看整合 →</a>
  </div>
</div>

---

## 已上架 SMART App Gallery

<div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0; border: 2px solid #4caf50;">
  <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
    <img src="{{ '/assets/images/smart-app-icon.png' | relative_url }}" alt="ThTxGNN App Icon" style="width: 64px; height: 64px; border-radius: 12px;">
    <div>
      <div style="font-weight: 600; font-size: 1.2rem; color: #2e7d32;">thtxgnn-smart-app</div>
      <div style="color: #555;">藥提醒科技有限公司</div>
    </div>
  </div>
  <p style="margin-bottom: 1rem; color: #333;">Query drug repurposing candidates for patient medications using TxGNN knowledge graph predictions.</p>
  <a href="https://apps.smarthealthit.org/app/thtxgnn-smart-app" target="_blank" style="display: inline-block; padding: 10px 20px; background: #333; color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">前往 SMART App Gallery 查看 ↗</a>
</div>

---

## 文件結構

| 頁面 | 說明 |
|------|------|
| [使用指南](guide/) | 圖文教學，適合一般使用者 |
| [技術文件](technical-docs/) | FHIR 配置、API 端點，適合開發者 |
| [整合資源](integrations/) | 外部資源整合與連結 |

---

## 免責聲明

<div style="background: #fff3cd; border: 1px solid #ffc107; border-radius: 8px; padding: 16px; margin: 20px 0;">
<strong>重要提醒</strong><br>
本網站內容僅供研究參考，不能取代專業醫療建議。所有藥物再利用預測結果需經過臨床驗證才能應用。如有健康問題，請諮詢合格醫療人員。
</div>

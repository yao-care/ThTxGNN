---
layout: default
title: 使用指南
parent: SMART on FHIR
nav_order: 1
description: "圖文教學：如何使用 ThTxGNN SMART App 從電子病歷系統讀取用藥並查詢老藥新用候選"
permalink: /smart/guide/
---

# 🏥 SMART on FHIR 使用指南

<p class="key-answer" data-question="如何使用 ThTxGNN SMART App？">
ThTxGNN SMART App 可以從電子病歷系統（EHR）讀取病患用藥，自動查詢老藥新用候選。本指南提供兩種使用方式：<strong>獨立測試模式</strong>（推薦初學者）與 <strong>SMART Launcher 測試</strong>。
</p>

---

## 🎉 已上架 SMART App Gallery

<p class="key-answer" data-question="ThTxGNN 是否已上架 SMART App Gallery？">
ThTxGNN SMART App 已正式上架至 <strong>SMART Health IT App Gallery</strong>，這是全球最大的 SMART on FHIR 應用程式目錄，收錄經過審核的醫療健康應用程式。
</p>

<div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0; border: 2px solid #4caf50;">
  <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
    <img src="{{ '/assets/images/smart-app-icon.png' | relative_url }}" alt="ThTxGNN App Icon" style="width: 64px; height: 64px; border-radius: 12px;">
    <div>
      <div style="font-weight: 600; font-size: 1.2rem; color: #2e7d32;">thtxgnn-smart-app</div>
      <div style="color: #555;">藥提醒科技有限公司</div>
    </div>
  </div>
  <p style="margin-bottom: 1rem; color: #333;">Query drug repurposing candidates for patient medications using TxGNN knowledge graph predictions.</p>
  <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 1rem;">
    <span style="padding: 4px 12px; background: #2196f3; color: white; border-radius: 16px; font-size: 0.85rem;">SMART App</span>
    <span style="padding: 4px 12px; background: #ff9800; color: white; border-radius: 16px; font-size: 0.85rem;">FHIR R4</span>
    <span style="padding: 4px 12px; background: #9c27b0; color: white; border-radius: 16px; font-size: 0.85rem;">Patients & Clinicians</span>
  </div>
  <a href="https://apps.smarthealthit.org/app/thtxgnn-smart-app" target="_blank" style="display: inline-block; padding: 10px 20px; background: #333; color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">前往 SMART App Gallery 查看 ↗</a>
</div>

### App Gallery 頁面截圖

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
  <div>
    <img src="{{ '/assets/images/smarthealthit_screenshot.png' | relative_url }}" alt="ThTxGNN SMART App Gallery 頁面" style="width: 100%; border-radius: 8px; border: 1px solid #e0e0e0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <p style="text-align: center; color: #666; font-size: 0.9rem; margin-top: 0.5rem;">App 詳細頁面</p>
  </div>
</div>

### App 規格

| 項目 | 內容 |
|------|------|
| **Application Type** | SMART App |
| **FHIR Compatibility** | R4 |
| **Designed for** | Patients & Clinicians |
| **Platform** | Web |
| **Pricing** | Free / Open Source |
| **Privacy Policy** | [https://thtxgnn.yao.care/privacy-policy/]({{ '/privacy-policy/' | relative_url }}) |

---

## 🏥 歡迎醫療機構整合測試

<p class="key-answer" data-question="如何將 ThTxGNN 整合到我們醫院的系統？">
若貴院的 EHR 系統支援 SMART on FHIR，歡迎使用以下方式進行整合測試。我們提供兩種測試模式，讓您的 IT 團隊可以快速驗證連接。
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); border-radius: 12px; border: 2px solid #4caf50;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
    <strong style="font-size: 1.1rem; color: #2e7d32;">方式一：獨立測試模式</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">不需要 EHR 連線，直接輸入藥物名稱測試功能</p>
    <span style="display: inline-block; padding: 4px 12px; background: #4caf50; color: white; border-radius: 16px; font-size: 0.85rem;">快速體驗</span>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); border-radius: 12px; border: 2px solid #2196f3;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔗</div>
    <strong style="font-size: 1.1rem; color: #1565c0;">方式二：SMART Launcher 測試</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">完整測試 OAuth 授權流程與 EHR 整合</p>
    <span style="display: inline-block; padding: 4px 12px; background: #2196f3; color: white; border-radius: 16px; font-size: 0.85rem;">IT 整合驗證</span>
  </div>
</div>

---

## 方式一：獨立測試模式

<p class="key-answer" data-question="如何使用獨立測試模式？">
獨立測試模式讓您不需要連接 EHR 系統，直接輸入藥物名稱即可測試 ThTxGNN 的藥物映射與老藥新用查詢功能。
</p>

### 步驟 1：開啟獨立測試頁面

<div style="background: #f8f9fa; border-radius: 8px; padding: 1.5rem; margin: 1rem 0;">
  <p style="margin-bottom: 1rem;">點擊下方按鈕開啟獨立測試頁面：</p>
  <div style="display: flex; flex-wrap: wrap; gap: 12px;">
    <a href="{{ '/smart/standalone.html' | relative_url }}?drugs=Famotidine,Docetaxel,Paclitaxel" target="_blank" style="display: inline-block; padding: 12px 24px; background: linear-gradient(135deg, #28a745 0%, #20c997 100%); color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">🚀 直接查看 L1 範例 ↗</a>
    <a href="{{ '/smart/standalone.html' | relative_url }}" target="_blank" style="display: inline-block; padding: 12px 24px; background: #e0e0e0; color: #333; text-decoration: none; border-radius: 8px; font-weight: 500;">開啟空白頁面 ↗</a>
  </div>
  <p style="margin-top: 1rem; font-size: 0.9rem; color: #666;">💡 點擊「直接查看 L1 範例」會自動載入 Famotidine、Docetaxel、Paclitaxel 三個 L1 證據等級藥物並顯示查詢結果</p>
</div>

頁面載入後，您會看到：

<div style="background: #fff; border: 1px solid #e0e0e0; border-radius: 12px; padding: 1.5rem; margin: 1rem 0;">
  <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
    <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">T</div>
    <div>
      <div style="font-weight: 600;">ThTxGNN SMART App</div>
      <div style="color: #666; font-size: 0.9rem;">獨立測試模式</div>
    </div>
  </div>
  <div style="background: #f5f5f5; border-radius: 8px; padding: 1rem;">
    <div style="color: #666; margin-bottom: 0.5rem;">已載入的 L1 範例藥物：</div>
    <div style="display: flex; flex-wrap: wrap; gap: 8px;">
      <span style="background: #667eea; color: white; padding: 6px 12px; border-radius: 20px; font-size: 14px;">Famotidine</span>
      <span style="background: #667eea; color: white; padding: 6px 12px; border-radius: 20px; font-size: 14px;">Docetaxel</span>
      <span style="background: #667eea; color: white; padding: 6px 12px; border-radius: 20px; font-size: 14px;">Paclitaxel</span>
    </div>
  </div>
</div>

### 步驟 2：查看或新增藥物

使用「直接查看 L1 範例」連結開啟時，系統會自動載入三個 L1 證據等級藥物。您也可以手動新增其他藥物：

| 輸入類型 | 範例 |
|----------|------|
| 英文學名 | Famotidine, Docetaxel, Paclitaxel |
| 中文名稱 | 法莫替丁, 多西他賽 |
| RxCUI 代碼 | 855332, 1161611 |

<div style="background: #e8f5e9; border-left: 4px solid #4caf50; padding: 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0;">
  <strong>💡 提示：</strong>建議使用英文學名以獲得最佳比對結果
</div>

### 步驟 3：查看老藥新用候選

點擊「查詢」按鈕後，系統會：

<ol class="actionable-steps">
  <li><strong>藥物名稱映射</strong>：將輸入的名稱比對到 ThTxGNN 資料庫</li>
  <li><strong>查詢預測結果</strong>：找出該藥物的老藥新用候選適應症</li>
  <li><strong>顯示證據等級</strong>：每個預測標示 L1-L5 證據等級</li>
</ol>

結果會自動顯示，例如 Famotidine：

<div style="background: #fff; border: 1px solid #e0e0e0; border-radius: 12px; padding: 1.5rem; margin: 1rem 0;">
  <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
    <span style="font-weight: 600; font-size: 1.1rem;">Famotidine</span>
    <span style="padding: 2px 8px; background: #2E7D32; color: white; border-radius: 4px; font-size: 0.8rem;">L1</span>
  </div>
  <div style="color: #666; margin-bottom: 1rem; font-size: 0.9rem;">原適應症：住院病人伴隨有病理性胃酸分泌過高之症狀，頑固性十二指腸潰瘍...</div>
  <div style="font-size: 0.9rem; font-weight: 500; margin-bottom: 0.5rem;">老藥新用候選：</div>
  <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
    <span style="padding: 4px 12px; background: #e8f5e9; color: #2e7d32; border-radius: 16px; font-size: 0.85rem;">duodenogastric reflux (99.99)</span>
    <span style="padding: 4px 12px; background: #e8f5e9; color: #2e7d32; border-radius: 16px; font-size: 0.85rem;">duodenal obstruction (99.99)</span>
    <span style="padding: 4px 12px; background: #e8f5e9; color: #2e7d32; border-radius: 16px; font-size: 0.85rem;">peptic ulcer perforation (99.98)</span>
    <span style="padding: 4px 12px; background: #fce4ec; color: #c2185b; border-radius: 16px; font-size: 0.85rem;">... 更多</span>
  </div>
</div>

---

## 方式二：SMART Launcher 測試

<p class="key-answer" data-question="如何使用 SMART Launcher 測試？">
SMART Launcher 是官方提供的測試工具，可以模擬 EHR 系統啟動 SMART App 的完整流程，包含 OAuth 2.0 授權。
</p>

### 步驟 1：前往 SMART Launcher

<div style="background: #f8f9fa; border-radius: 8px; padding: 1.5rem; margin: 1rem 0;">
  <p style="margin-bottom: 1rem;">點擊下方連結開啟已預先設定好的 SMART Launcher：</p>
  <a href="https://launch.smarthealthit.org/?launch_url=https%3A%2F%2Fthtxgnn.yao.care%2Fsmart%2Flaunch.html&launch=WzAsIiIsIiIsIkFVVE8iLDAsMCwwLCIiLCIiLCIiLCIiLCIiLCIiLCIiLDAsMSwiIl0" target="_blank" style="display: inline-block; padding: 12px 24px; background: #333; color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">🚀 前往 SMART Launcher（已設定好）↗</a>
  <p style="margin-top: 1rem; font-size: 0.9rem; color: #666;">💡 連結已自動設定 Launch URL，只需選擇病患即可開始測試</p>
</div>

### 步驟 2：選擇測試病患

開啟後，Launch URL 已自動設定完成。接下來：

1. 展開 **Select Patient(s)** 區塊
2. 使用篩選條件找到有用藥記錄的病患：
   - **Conditions**: 選擇有慢性病（如 Hypertension）的病患
   - **Medications**: 確認病患有用藥記錄

<div style="background: #fff3e0; border-left: 4px solid #ff9800; padding: 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0;">
  <strong>⚠️ 注意：</strong>SMART Launcher 使用 Synthea 合成資料（美國藥品），部分藥物可能無法與 ThTxGNN 資料庫（泰國健保藥品）完全匹配。
</div>

<div style="background: #e8f5e9; border-left: 4px solid #4caf50; padding: 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0;">
  <strong>💡 推薦測試藥物：</strong>以下藥物在 ThTxGNN 有 L1 等級預測，且可能出現在美國測試資料中：
  <ul style="margin: 0.5rem 0 0 1.5rem;">
    <li>Famotidine（胃酸抑制劑）</li>
    <li>Vitamin E（維生素補充劑）</li>
    <li>Isosorbide dinitrate（心絞痛用藥）</li>
  </ul>
</div>

### 步驟 3：啟動並授權

1. 點擊 **Launch** 按鈕
2. 頁面會跳轉到 ThTxGNN SMART App
3. 如果出現授權頁面，點擊 **Authorize** 授權存取
4. 系統會自動讀取病患用藥並顯示老藥新用候選

---

## 流程比較

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background: #f5f5f5;">
      <th style="padding: 12px; text-align: left; border: 1px solid #e0e0e0;">比較項目</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">🎯 獨立測試模式</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">🔗 SMART Launcher</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border: 1px solid #e0e0e0;">需要連線</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">❌ 不需要</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">✅ 需要</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #e0e0e0;">OAuth 授權</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">❌ 不測試</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">✅ 完整測試</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #e0e0e0;">藥物來源</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">手動輸入</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">EHR 自動讀取</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #e0e0e0;">藥物匹配率</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">✅ 高（可指定）</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">⚠️ 低（美國藥品）</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #e0e0e0;">適合對象</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">一般使用者</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #e0e0e0;">開發者 / IT 人員</td>
    </tr>
  </tbody>
</table>

---

## 常見問題

### 為什麼有些藥物顯示「無法匹配」？

ThTxGNN 資料庫以**泰國健保藥品**為主，而 SMART Launcher 使用的是**美國 Synthea 合成資料**。部分藥物名稱不同或泰國未核准，因此無法匹配。

**解決方案**：使用獨立測試模式，直接輸入 ThTxGNN 資料庫中的藥物名稱。

### 如何在正式 EHR 系統中使用？

請聯繫您的 EHR 系統管理員，提供以下資訊進行配置：

| 項目 | 值 |
|------|------|
| Launch URL | `https://thtxgnn.yao.care/smart/launch.html` |
| Redirect URI | `https://thtxgnn.yao.care/smart/app.html` |
| Client ID | `thtxgnn-smart-app` |
| Scopes | `launch patient/MedicationRequest.read openid fhirUser` |

### 病患資料安全嗎？

是的。ThTxGNN SMART App：
- **不儲存**任何病患資料
- 所有處理都在**瀏覽器端**進行
- 使用 **PKCE** 保護 OAuth 流程
- 只請求**最小必要權限**

---

## 技術文件

需要更詳細的技術規格？請參考：

<div style="margin: 1rem 0;">
  <a href="{{ '/smart/' | relative_url }}" style="display: inline-block; padding: 10px 20px; background: #f5f5f5; color: #333; text-decoration: none; border-radius: 8px; border: 1px solid #e0e0e0;">📚 SMART on FHIR 技術文件</a>
</div>

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本網站內容僅供研究參考，不能取代專業醫療建議。所有藥物再利用預測結果需經過臨床驗證才能應用。如有健康問題，請諮詢合格醫療人員。
</div>

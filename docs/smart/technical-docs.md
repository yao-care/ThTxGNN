---
layout: default
title: 技術文件
parent: SMART on FHIR
nav_order: 2
description: ThTxGNN SMART on FHIR 技術規格，包含 OAuth 配置、FHIR API 端點、藥物映射流程
permalink: /smart/technical-docs/
---

# SMART on FHIR 技術文件

本頁面提供 ThTxGNN SMART App 的技術規格，供開發者和 IT 人員參考。

---

## 技術規格

### SMART on FHIR 配置

| 項目 | 值 |
|------|------|
| FHIR 版本 | R4 |
| Client ID | `thtxgnn-smart-app` |
| Launch URI | `/smart/launch.html` |
| Redirect URI | `/smart/app.html` |
| 授權方式 | OAuth 2.0 with PKCE |

### 請求的權限範圍（Scopes）

```
launch
patient/MedicationRequest.read
patient/MedicationStatement.read
openid
fhirUser
```

### 藥物映射流程

<div style="display: flex; flex-direction: column; align-items: center; gap: 0; margin: 2rem 0;">
  <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 12px 24px; border-radius: 8px; font-weight: 600; text-align: center;">
    EHR MedicationRequest
  </div>
  <div style="width: 2px; height: 24px; background: #667eea;"></div>
  <div style="width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 10px solid #667eea;"></div>

  <div style="background: #f8f9fa; border: 2px solid #e0e0e0; padding: 12px 24px; border-radius: 8px; text-align: center; margin-top: -5px;">
    <strong>1. 提取 RxCUI</strong><br>
    <span style="color: #666; font-size: 0.9rem;">RxNorm 藥物代碼</span>
  </div>
  <div style="width: 2px; height: 16px; background: #e0e0e0;"></div>
  <div style="width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 8px solid #e0e0e0;"></div>

  <div style="background: #f8f9fa; border: 2px solid #e0e0e0; padding: 12px 24px; border-radius: 8px; text-align: center; margin-top: -5px;">
    <strong>2. RxNorm API</strong><br>
    <span style="color: #666; font-size: 0.9rem;">取得藥物成分名</span>
  </div>
  <div style="width: 2px; height: 16px; background: #e0e0e0;"></div>
  <div style="width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 8px solid #e0e0e0;"></div>

  <div style="background: #f8f9fa; border: 2px solid #e0e0e0; padding: 12px 24px; border-radius: 8px; text-align: center; margin-top: -5px;">
    <strong>3. 名稱正規化</strong><br>
    <span style="color: #666; font-size: 0.9rem;">移除鹽類後綴、同義詞對照</span>
  </div>
  <div style="width: 2px; height: 16px; background: #e0e0e0;"></div>
  <div style="width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 8px solid #e0e0e0;"></div>

  <div style="background: #f8f9fa; border: 2px solid #e0e0e0; padding: 12px 24px; border-radius: 8px; text-align: center; margin-top: -5px;">
    <strong>4. Fuse.js 模糊比對</strong><br>
    <span style="color: #666; font-size: 0.9rem;">比對 ThTxGNN 資料庫</span>
  </div>
  <div style="width: 2px; height: 24px; background: #28a745;"></div>
  <div style="width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 10px solid #28a745;"></div>

  <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%); color: white; padding: 12px 24px; border-radius: 8px; font-weight: 600; text-align: center; margin-top: -5px;">
    顯示老藥新用候選
  </div>
</div>

---

## FHIR API

ThTxGNN 提供靜態 FHIR API，讓其他系統可以查詢藥物預測資料。

### 端點

| 端點 | 說明 |
|------|------|
| `/fhir/metadata` | CapabilityStatement |
| `/fhir/MedicationKnowledge/{id}.json` | 單一藥物資源 |
| `/fhir/Bundle/all-predictions.json` | 全部預測結果 |

### 範例

```bash
# 取得 Warfarin 的藥物知識資源
curl https://thtxgnn.yao.care/fhir/MedicationKnowledge/warfarin.json
```

---

## 測試環境

### 使用 SMART Health IT Launcher 測試

1. 前往 [SMART Launcher](https://launch.smarthealthit.org/)
2. 設定：
   - **Launch Type**: Provider EHR Launch
   - **FHIR Version**: R4
   - **App Launch URL**: `https://thtxgnn.yao.care/smart/launch.html`
3. 選擇測試病患
4. 點擊 Launch 開始測試

### 支援的 EHR 系統

理論上支援所有符合 SMART on FHIR R4 標準的 EHR 系統，包括：

- Epic
- Cerner (Oracle Health)
- Allscripts
- 其他 FHIR R4 相容系統

---

## 隱私與安全

- **無資料儲存**：應用程式不會在伺服器端儲存任何病患資料
- **純前端處理**：所有資料處理都在瀏覽器中進行
- **PKCE 保護**：使用 OAuth 2.0 PKCE 流程確保授權安全
- **最小權限**：只請求必要的讀取權限

詳細資訊請參閱 [隱私權政策](/privacy-policy/)

---

## 相關連結

- [SMART on FHIR 官方文件](http://docs.smarthealthit.org/)
- [HL7 FHIR 規範](https://www.hl7.org/fhir/)
- [RxNorm API 文件](https://lhncbc.nlm.nih.gov/RxNav/APIs/RxNormAPIs.html)

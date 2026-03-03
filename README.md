# ThTxGNN - ระบบคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่สำหรับประเทศไทย

[![Website](https://img.shields.io/badge/Website-thtxgnn.yao.care-blue)](https://thtxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ใช้โมเดล TxGNN Knowledge Graph จาก Harvard เพื่อคาดการณ์ข้อบ่งใช้ใหม่ (Drug Repurposing) สำหรับยาที่ขึ้นทะเบียนกับสำนักงานคณะกรรมการอาหารและยา (อย.) ประเทศไทย

## ⚠️ ข้อควรระวัง

- ผลการคาดการณ์นี้ **มีไว้เพื่อการวิจัยเท่านั้น** ไม่ถือเป็นคำแนะนำทางการแพทย์
- การใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการทดลองทางคลินิกและได้รับอนุมัติจากหน่วยงานที่เกี่ยวข้อง

## ภาพรวมโครงการ

### สถิติการคาดการณ์

| รายการ | จำนวน |
|--------|-------|
| **ยาที่วิเคราะห์** | 151 รายการ |
| **การคาดการณ์ทั้งหมด** | 2,573,191 คู่ |
| **การคาดการณ์ความเชื่อมั่นสูง (≥0.9)** | 11,033 รายการ |
| **แหล่งข้อมูลยา** | Thai FDA (อย.) |

### การกระจายตามระดับหลักฐาน

| ระดับหลักฐาน | คำอธิบาย | การตัดสินใจ |
|:------------:|----------|-------------|
| **L1** | ผ่านการตรวจสอบทางคลินิก | ผ่านการตรวจสอบ |
| **L2** | หลักฐานแข็งแกร่ง (Clinical Trial + Literature) | ดำเนินการต่อด้วยความระมัดระวัง |
| **L3** | หลักฐานปานกลาง | ดำเนินการต่อด้วยความระมัดระวัง |
| **L4** | หลักฐานอ่อน (คะแนนโมเดลสูง) | รอหลักฐานเพิ่มเติม |
| **L5** | การคาดการณ์จากโมเดลเท่านั้น | รอหลักฐานเพิ่มเติม |

---

## วิธีการคาดการณ์

มีสองวิธีในการคาดการณ์ตามแนวทางของ TxGNN:

| วิธี | ความเร็ว | ความแม่นยำ | ความต้องการระบบ | ไฟล์ผลลัพธ์ |
|------|----------|------------|-----------------|-------------|
| Knowledge Graph | เร็ว (ไม่กี่วินาที) | ต่ำกว่า | ไม่มีความต้องการพิเศษ | `repurposing_candidates.csv` |
| Deep Learning | ช้า (หลายชั่วโมง) | สูงกว่า | Conda + PyTorch + DGL | `txgnn_dl_predictions.csv` |

### วิธี Knowledge Graph

```bash
uv run python scripts/run_kg_prediction.py
```

ค้นหาความสัมพันธ์ยา-โรคโดยตรงจาก TxGNN Knowledge Graph

**ผลลัพธ์**: `data/processed/repurposing_candidates.csv`

| ตัวชี้วัด | ค่า |
|-----------|-----|
| จำนวนยาทั้งหมดจาก Thai FDA | 155 |
| จำนวนยาที่ map ได้กับ DrugBank | 151 (97.42%) |
| อัตราการ map ข้อบ่งใช้ | 83.63% |
| จำนวนการคาดการณ์ | 1,115 |

### วิธี Deep Learning

```bash
# ใช้ conda environment (ต้องติดตั้ง PyTorch + DGL ก่อน)
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

ใช้โมเดล Neural Network ที่ผ่านการ pretrain จาก TxGNN เพื่อคำนวณคะแนนความน่าจะเป็น

**ผลลัพธ์**: `data/processed/txgnn_dl_predictions.csv`

| ตัวชี้วัด | ค่า |
|-----------|-----|
| จำนวนการคาดการณ์ทั้งหมด | 2,573,191 |
| จำนวนยาที่เกี่ยวข้อง | 151 |
| จำนวนข้อบ่งใช้ที่เกี่ยวข้อง | 17,041 |
| การคาดการณ์ความเชื่อมั่นสูง (>0.9) | 11,033 |

### การตีความคะแนน TxGNN

คะแนน TxGNN แสดงความเชื่อมั่นของโมเดลสำหรับคู่ "ยา-โรค" อยู่ในช่วง 0-1

| เกณฑ์ | จำนวน | ความหมาย |
|-------|-------|----------|
| ≥ 0.9999 | ~500 | ความเชื่อมั่นสูงมาก โมเดลมั่นใจที่สุด |
| ≥ 0.999 | ~2,500 | ความเชื่อมั่นสูงมาก |
| ≥ 0.99 | ~15,000 | ความเชื่อมั่นสูง ควรตรวจสอบเป็นอันดับแรก |
| ≥ 0.9 | ~11,000 | ความเชื่อมั่นปานกลาง-สูง |

#### ข้อควรจำ

1. **คะแนนสูงไม่ได้หมายความว่ามีประสิทธิผลทางคลินิก**: คะแนน TxGNN เป็นการคาดการณ์จาก Knowledge Graph ต้องมีการทดลองทางคลินิกยืนยัน
2. **คะแนนต่ำไม่ได้หมายความว่าไม่มีประสิทธิผล**: โมเดลอาจยังไม่ได้เรียนรู้ความสัมพันธ์บางอย่าง
3. **แนะนำให้ใช้ร่วมกับกระบวนการตรวจสอบ**: ตรวจสอบหลักฐานจาก Clinical Trials และวรรณกรรมประกอบ

---

## การเริ่มต้นใช้งาน

### ขั้นตอนที่ 1: ดาวน์โหลดข้อมูล

| ไฟล์ | ลิงก์ดาวน์โหลด | ตำแหน่ง | การใช้งาน |
|------|----------------|---------|-----------|
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | `data/node.csv` | ข้อมูล Node |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | `data/kg.csv` | Knowledge Graph |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | `data/edges.csv` | ข้อมูล Edge (สำหรับ Deep Learning) |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | แตกไฟล์ไปที่ `model_ckpt/` | โมเดลที่ pretrain แล้ว (สำหรับ Deep Learning) |

### ขั้นตอนที่ 2: ติดตั้ง Environment

```bash
# ติดตั้ง dependencies
uv sync

# ทดสอบโปรแกรม
uv run pytest tests/
```

### ขั้นตอนที่ 3: ดึงข้อมูลยาจาก Thai FDA

```bash
uv run python scripts/fetch_thaifda_drugs.py
```

### ขั้นตอนที่ 4: ประมวลผลข้อมูล FDA

```bash
uv run python scripts/process_fda_data.py
```

### ขั้นตอนที่ 5: เตรียมข้อมูล Vocabulary

```bash
uv run python scripts/prepare_external_data.py
```

ไฟล์ที่สร้าง:
- `data/external/drugbank_vocab.csv` - รายการยาจาก DrugBank
- `data/external/disease_vocab.csv` - รายการโรค
- `data/external/drug_disease_relations.csv` - ความสัมพันธ์ยา-โรค

### ขั้นตอนที่ 6: รันการคาดการณ์ Knowledge Graph

```bash
uv run python scripts/run_kg_prediction.py
```

### ขั้นตอนที่ 7: ติดตั้ง Environment สำหรับ Deep Learning (ไม่บังคับ)

```bash
# 1. สร้าง conda environment
conda create -n txgnn python=3.11 -y
conda activate txgnn

# 2. ติดตั้ง PyTorch
pip install torch==2.2.2 torchvision==0.17.2

# 3. ติดตั้ง DGL
pip install dgl==1.1.3

# 4. ติดตั้ง TxGNN
pip install git+https://github.com/mims-harvard/TxGNN.git

# 5. ติดตั้ง dependencies อื่นๆ
pip install pandas tqdm pyyaml pydantic ogb

# 6. ตรวจสอบการติดตั้ง
python -c "import torch; import dgl; import txgnn; print('ติดตั้งสำเร็จ!')"
```

### ขั้นตอนที่ 8: รันการคาดการณ์ Deep Learning

```bash
# แตกไฟล์โมเดล
unzip -n model_ckpt.zip

# เปิดใช้งาน conda environment และรันการคาดการณ์
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

---

## โครงสร้างโปรเจค

```
ThTxGNN/
├── README.md                    # เอกสารโปรเจค
├── CLAUDE.md                    # คู่มือ AI Assistant
├── pyproject.toml               # การตั้งค่า Python Package
│
├── data/                        # ไดเรกทอรีข้อมูล
│   ├── kg.csv                   # 🟡 TxGNN Knowledge Graph
│   ├── node.csv                 # 🟡 TxGNN Node Data
│   ├── edges.csv                # 🟡 TxGNN Edge Data
│   ├── raw/
│   │   └── th_fda_drugs.json    # 🟢 ข้อมูลยาจาก Thai FDA
│   ├── external/                # 🔵 สร้างจาก prepare_external_data.py
│   │   ├── drugbank_vocab.csv
│   │   ├── disease_vocab.csv
│   │   └── drug_disease_relations.csv
│   └── processed/
│       ├── drug_mapping.csv            # 🔵 การ map ยาไทย→DrugBank
│       ├── indication_mapping.csv      # 🔵 การ map ข้อบ่งใช้→โรค
│       ├── repurposing_candidates.csv  # 🔵 ผลลัพธ์ Knowledge Graph
│       └── txgnn_dl_predictions.csv    # 🔵 ผลลัพธ์ Deep Learning
│
├── model_ckpt/                  # 🟡 TxGNN Pretrained Model
│
├── src/thtxgnn/                 # 🔵 Source Code
│   ├── data/
│   │   └── loader.py            # โหลดข้อมูล FDA
│   ├── mapping/
│   │   ├── normalizer.py        # การทำให้ชื่อยาเป็นมาตรฐาน
│   │   ├── drugbank_mapper.py   # การ map DrugBank ID
│   │   └── disease_mapper.py    # การ map ข้อบ่งใช้→โรค
│   ├── predict/
│   │   ├── repurposing.py       # การคาดการณ์ Knowledge Graph
│   │   └── txgnn_model.py       # การคาดการณ์ Deep Learning
│   └── collectors/              # เครื่องมือเก็บข้อมูลหลักฐาน
│
├── scripts/                     # 🔵 สคริปต์ทำงาน
│   ├── fetch_thaifda_drugs.py   # ดึงข้อมูลจาก Thai FDA
│   ├── process_fda_data.py      # ประมวลผลข้อมูล FDA
│   ├── prepare_external_data.py # เตรียม Vocabulary
│   ├── run_kg_prediction.py     # รัน Knowledge Graph
│   └── run_txgnn_prediction.py  # รัน Deep Learning
│
├── docs/                        # 🔵 เว็บไซต์ (Jekyll)
│   ├── _drugs/                  # รายงานยารายตัว
│   ├── fhir/                    # FHIR Resources
│   └── smart/                   # SMART on FHIR App
│
└── tests/                       # 🔵 Unit Tests
```

**สัญลักษณ์**: 🔵 พัฒนาในโปรเจค | 🟢 ข้อมูลไทย | 🟡 ข้อมูล TxGNN

---

## แหล่งข้อมูลที่เกี่ยวข้อง

- [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x) - บทความต้นฉบับ
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN) - Source Code ต้นฉบับ
- [TxGNN Explorer](http://txgnn.org) - เครื่องมือค้นหาแบบ Interactive

| ข้อมูล | แหล่งที่มา | คำอธิบาย |
|--------|------------|----------|
| ยาไทย | [Thai FDA (อย.)](https://www.fda.moph.go.th/) | ข้อมูลยาที่ขึ้นทะเบียนในประเทศไทย |
| TxGNN Knowledge Graph | [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM) | 17,080 โรค, 7,957 ยา |

---

## การอ้างอิง

หากคุณใช้ข้อมูลหรือซอฟต์แวร์จากโปรเจคนี้ กรุณาอ้างอิง:

```bibtex
@software{thtxgnn2026,
  author       = {Yao.Care},
  title        = {ThTxGNN: Drug Repurposing Predictions for Thailand FDA Drugs},
  year         = 2026,
  url          = {https://github.com/yao-care/ThTxGNN}
}
```

และอ้างอิงบทความ TxGNN ต้นฉบับ:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and Chandak, Payal and Wang, Qianwen and Haber, Shreyas and Zitnik, Marinka},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

## License

MIT License - ดูรายละเอียดใน [LICENSE](LICENSE)

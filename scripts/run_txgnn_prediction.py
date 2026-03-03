#!/usr/bin/env python3
"""TxGNN 泰國藥品老藥新用預測 - 深度學習方法

此腳本使用 TxGNN 預訓練模型執行深度學習預測，
自動偵測可用的運算裝置（CUDA/CPU）。
支援中斷續算：中途按 Ctrl+C 中斷後，重新執行會自動從上次中斷處繼續。

前置條件:
    1. 下載並解壓縮 model_ckpt.zip 到 model_ckpt/ 目錄
    2. 設定 conda 環境（參考 README.md 步驟 5）

使用方法:
    # 啟動 conda 環境並執行
    conda activate txgnn
    python scripts/run_txgnn_prediction.py

    # 忽略之前的進度，重新開始
    python scripts/run_txgnn_prediction.py --restart

環境設定（詳見 README.md）:
    conda create -n txgnn python=3.11 -y
    conda activate txgnn
    pip install torch==2.2.2 torchvision==0.17.2
    pip install dgl==1.1.3
    pip install git+https://github.com/mims-harvard/TxGNN.git
    pip install pandas tqdm pyyaml pydantic ogb
"""

import argparse
import sys
from pathlib import Path

# 將 src 加入 Python 路徑
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from thtxgnn.predict.txgnn_model import (
    check_dependencies,
    detect_device,
    print_install_instructions,
    run_taiwan_drug_prediction,  # 函數名稱保持相容，實際上對泰國藥品也適用
)


def main():
    parser = argparse.ArgumentParser(description="TxGNN 泰國藥品老藥新用預測")
    parser.add_argument(
        "--restart",
        action="store_true",
        help="忽略之前的進度，重新開始預測",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("TxGNN 泰國藥品老藥新用預測 (ThTxGNN)")
    print("=" * 60)
    print()

    # 偵測裝置
    device = detect_device()

    # 檢查依賴
    deps_ok, missing = check_dependencies()

    if not deps_ok:
        print(f"\n缺少必要套件: {', '.join(missing)}")
        print_install_instructions(missing, device)
        print("\n請安裝上述套件後重新執行此腳本。")
        sys.exit(1)

    print()

    # 執行預測（支援中斷續算）
    result = run_taiwan_drug_prediction(
        device=device,
        min_score=0.0,  # 保留所有正分數結果
        restart=args.restart,
    )

    if result is not None and len(result) > 0:
        print("\n預測完成！")
        print(f"結果檔案: data/processed/txgnn_dl_predictions.csv")
        print(f"Checkpoint: data/processed/txgnn_checkpoint.csv")
    else:
        print("\n預測未產生結果，請檢查藥品映射資料。")


if __name__ == "__main__":
    main()

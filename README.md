# Obfuscated Malware Memory Detection (CIC-MalMem-2022)

An end-to-end Machine Learning pipeline designed to detect obfuscated malware in volatile memory dumps using the **CIC-MalMem-2022** dataset. This repository benchmarked three classification algorithms (**Logistic Regression**, **Random Forest**, and **XGBoost**) to identify malicious processes based on memory artifacts.

---

## 📊 Dataset Overview

* **Dataset:** CIC-MalMem-2022
* **Total Instances:** 58,062 (after deduplication and cleaning)
* **Features:** 55 numerical memory forensic metrics
* **Target Classes:** Balanced binary distribution
  * `0`: Benign (Clean process memory)
  * `1`: Malware (Obfuscated malware memory)

---

## 🛠️ Project Structure

```text
├── data/               # Raw dataset references
├── models/             # Trained serialized model (best_model.pkl)
├── results/            # Performance metrics CSV and evaluation plots
├── src/                # Modular Python source code
│   └── preprocess.py   # Preprocessing and scaling module
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## 📈 Model Performance & Evaluation

All candidate models were evaluated on an **80/20 train/test split** (46,449 training samples, 11,613 test samples) with stratified sampling and feature scaling via `StandardScaler`.

### Benchmark Results

| Model | Accuracy | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 0.9991 | 0.9997 | 0.9986 | 0.9991 |
| **Random Forest** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |
| **XGBoost** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |

---

## 🔍 Key Findings & Feature Importance

Memory forensics analysis revealed that the number of services identified during memory inspection (`svcscan.nservices`) serves as the single most critical feature for detecting obfuscated malware, driving over **97%** of the decision-making weight in tree-based gradient boosted models.

* **Top Primary Indicator:** `svcscan.nservices` (~97.2% importance weight)
* **Secondary Indicators:** `svcscan.process_services`, `handles.avg_handles_per_proc`, `callbacks.ncallbacks` 

---

## 🚀 How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/CIC-MalMem-2022-Detection.git](https://github.com/YOUR_USERNAME/CIC-MalMem-2022-Detection.git)
   cd CIC-MalMem-2022-Detection
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run model loading:**
   ```bash
   python -c "import joblib; model = joblib.load('models/best_model.pkl'); print(model)"
   ```
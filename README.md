# Obfuscated Malware Detection (CIC-MalMem-2022)

A machine learning project for detecting obfuscated malware in memory dumps using the CIC-MalMem-2022 dataset. It evaluates Logistic Regression, Random Forest, and XGBoost models on memory forensic features.

## Dataset & Leakage Considerations

* **Source:** CIC-MalMem-2022 dataset.
* **Instances:** 58,062 clean samples (after strict deduplication to prevent data leakage).
* **Features:** 55 numerical memory forensic indicators.
* **Class Distribution:** Balanced binary classification (0: Benign, 1: Malware).

> **Data Leakage Mitigation:** To ensure realistic generalization, duplicates were stripped, stratified 80/20 train/test splitting was executed prior to any scaling, and `StandardScaler` was fitted strictly on the training set.

## Repository Layout

* `notebook.ipynb`: End-to-end execution pipeline (Data preprocessing, model training, evaluation, and visualizations).
* `src/preprocess.py`: Modular preprocessing and feature scaling logic.
* `models/best_model.pkl`: Serialized XGBoost model artifact.
* `results/`: Performance metrics CSV, ROC curves, and confusion matrices.
* `requirements.txt`: Python package dependencies.

## Benchmarks & Evaluation

Evaluated on an independent $20\%$ hold-out test set ($11,613$ samples):

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | False Negatives |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Logistic Regression | 0.9991 | 0.9997 | 0.9986 | 0.9991 | 0.9999 | 8 |
| Random Forest | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0 |
| XGBoost | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0 |

*Full Confusion Matrices and ROC Curves are stored under `results/`.*

## Forensic Insight: `svcscan.nservices`

Feature importance analysis identified `svcscan.nservices` as the primary classification signal (contributing $>97\%$ weight in XGBoost). 

**Security Interpretation:** Modern obfuscated malware injects malicious code into background system services or creates rogue services to maintain persistence and bypass standard process monitors. A high anomaly in service counts relative to standard execution profiles serves as a definitive behavioral artifact in memory dumps.

## Future Work

* **Explainable AI (XAI):** Integrating SHAP (SHapley Additive exPlanations) to provide local interpretability for security analysts per memory sample.
* **Adversarial Robustness:** Testing tree ensembles against feature perturbation techniques designed to mimic benign service signatures.

## Usage

1. Install dependencies:
   `pip install -r requirements.txt`

2. Run the experiment:
   Execute `notebook.ipynb`

# Obfuscated Malware Detection (CIC-MalMem-2022)

A machine learning project for detecting obfuscated malware in memory dumps using the CIC-MalMem-2022 dataset. It evaluates Logistic Regression, Random Forest, and XGBoost models on memory forensic features.

## Dataset

* Source: CIC-MalMem-2022
* Size: 58,062 instances (after removing duplicates)
* Features: 55 numerical features
* Target: Binary classification (0: Benign, 1: Malware)

## Repository Layout

* `notebook.ipynb`: Full execution code for data loading, model training, and evaluation.
* `src/preprocess.py`: Data cleaning, splitting, and scaling logic.
* `models/best_model.pkl`: Saved XGBoost model.
* `results/`: Metrics CSV and generated evaluation plots.
* `requirements.txt`: Python dependencies.

## Results

Evaluation on an 80/20 train/test split:

| Model | Accuracy | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| Logistic Regression | 0.9991 | 0.9997 | 0.9986 | 0.9991 |
| Random Forest | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| XGBoost | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

Feature importance analysis showed that `svcscan.nservices` is the primary feature used by the tree models, accounting for over 97% of the importance weight in XGBoost.

## Usage

1. Install requirements:
   pip install -r requirements.txt

2. Run the full experiment:
   Open and execute `notebook.ipynb`

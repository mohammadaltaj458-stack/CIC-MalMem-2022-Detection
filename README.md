# Obfuscated Malware Detection using Machine Learning

This project explores the use of machine learning techniques for detecting obfuscated malware using memory-based features from the CIC-MalMem-2022 dataset.

The goal of this project was to build and compare different machine learning models and understand how well they can classify benign and malicious memory samples.

## Dataset

Dataset: CIC-MalMem-2022

- Samples: 58,062 instances after removing duplicate records
- Features: 55 numerical memory-related features
- Task: Binary classification
    - 0: Benign
    - 1: Malware

## Approach

The project follows a simple machine learning pipeline:

1. Data cleaning and preprocessing
2. Removing duplicate samples
3. Splitting data into training and testing sets
4. Feature scaling using StandardScaler
5. Training and comparing different models:

- Logistic Regression
- Random Forest
- XGBoost

## Results

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

| Model | Accuracy | Precision | Recall | F1-score |
|------|----------|-----------|--------|----------|
| Logistic Regression | 0.9991 | 0.9997 | 0.9986 | 0.9991 |
| Random Forest | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| XGBoost | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

## Observations

The tree-based models achieved very high performance on this dataset.

Feature importance analysis showed that `svcscan.nservices` was one of the most influential features for XGBoost classification.

This suggests that service-related memory features may contain useful information for distinguishing between benign and malicious samples.

## Future Improvements

Possible future extensions include:

- Using SHAP to better understand model decisions.
- Testing model robustness under modified input features.
- Exploring deep learning approaches for malware detection.

## How to Run

Install dependencies:

pip install -r requirements.txt

Run:

Open and execute `notebook.ipynb`

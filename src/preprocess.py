import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(dataset_path):
    csv_file = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path) if f.endswith('.csv')][0]
    df = pd.read_csv(csv_file)
    
    df = df.drop_duplicates().dropna()
    
    if 'Category' in df.columns:
        df = df.drop(columns=['Category'])
        
    df['Class'] = df['Class'].map({'Benign': 0, 'Malware': 1})
    
    X = df.drop(columns=['Class']).select_dtypes(include=[np.number])
    y = df['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, X.columns

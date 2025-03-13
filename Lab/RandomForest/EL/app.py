import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Random Forest Classifier App')

st.sidebar.header('Upload your Excel file')
uploaded_file = st.sidebar.file_uploader('Upload an Excel file', type=['xlsx'])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, header=1)
    st.write('### Dataset Preview')
    st.write(df.head())

    # Data Preprocessing
    df.dropna(inplace=True)
    X = df.drop(['Sl No ', 'USN ', 'Name ', 'Title ', 'Grade'], axis=1)
    y = LabelEncoder().fit_transform(df['Grade'])

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Model Training
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    # Evaluation Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    st.write(f'### Accuracy: {accuracy:.4f}')
    st.write(f'### Precision: {precision:.4f}')
    st.write(f'### Recall: {recall:.4f}')
    st.write(f'### F1 Score: {f1:.4f}')

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    st.pyplot(fig)


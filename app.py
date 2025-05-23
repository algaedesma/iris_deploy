# -*- coding: utf-8 -*-
"""Streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13uMe8BrQJlpitxk3fX2GM62hgndQQdj_
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.datasets import load_iris

# Load model and data
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['target_name'] = df['target'].apply(lambda x: iris.target_names[x])

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["📊 Data Description", "🔍 Prediction", "📘 About the Project"])

# Page 1: Data Description
if page == "📊 Data Description":
    st.title("📊 Iris Dataset Overview")
    st.write("This page shows the basic information about the famous Iris dataset.")
    st.dataframe(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())

    st.subheader("Class Distribution")
    st.bar_chart(df['target_name'].value_counts())

# Page 2: Prediction
elif page == "🔍 Prediction":
    st.title("🔍 Iris Classification Prediction")

    sepal_length = st.slider("Sepal Length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
    sepal_width = st.slider("Sepal Width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
    petal_length = st.slider("Petal Length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
    petal_width = st.slider("Petal Width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

    if st.button("Predict"):
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)[0]
        st.success(f"The predicted Iris species is **{iris.target_names[prediction].capitalize()}**.")

# Page 3: About the Project
elif page == "📘 About the Project":
    st.title("📘 About This Project")

    st.markdown("""
    ### 🎯 Project Goal
    This project is created to demonstrate how a simple **Naive Bayes Classification** model can be deployed using **Streamlit**.

    ### 🧠 Methodology
    - Dataset: Iris dataset from sklearn.
    - Model: Gaussian Naive Bayes classifier.
    - Interface: Built using Streamlit with three interactive pages.

    ### 🚀 Features
    - View dataset and class distribution.
    - Input flower measurements to predict the species.
    - Understand how machine learning can be made accessible through a simple web app.

    ### 👤 Developer
    Developed by a data enthusiast as a part of a machine learning deployment exercise.

    """)
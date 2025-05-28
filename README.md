# 🚗 Auctioned Car Risk Prediction: Don't Get Kicked!

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thoufiqz55/Auctioned_car/blob/main/Used_cars_classification.ipynb)

> **Predict if a used car bought at an auction is a "bad buy" before you get kicked!**

---

## 📌 Overview

This project solves a real-world classification problem where dealerships want to avoid financial losses by identifying high-risk used cars *before* purchasing them at auctions. Based on the Kaggle competition **[Don't Get Kicked](https://www.kaggle.com/competitions/DontGetKicked)**, we predict whether a purchased vehicle will end up being a poor investment.

---

## 📊 Sample Output

![EDA Output](https://i.imgur.com/Y0X8dsA.jpg)
> *Pie chart showing auction purchase distribution*

---

## 📁 Dataset

- Source: [Kaggle - Don't Get Kicked](https://www.kaggle.com/competitions/DontGetKicked)
- Data fields: `VehicleAge`, `Make`, `Model`, `Odometer`, `Auction`, `VehicleCondition`, `IsBadBuy` (target), and others.

---

## 🧠 Project Workflow

- 📊 Exploratory Data Analysis (Seaborn, Plotly)
- 🔧 Feature Engineering
- 🤖 Model Training: Logistic Regression, Random Forest, XGBoost
- 📈 Model Evaluation: Accuracy, Confusion Matrix, F1 Score

---

## 🚀 Run It Yourself

### ⚙️ Installation
```bash
git clone https://github.com/thoufiqz55/Auctioned_car.git
cd Auctioned_car
pip install -r requirements.txt

---
🧪 Usage
Download the dataset from Kaggle and place it in the DontGetKicked/ directory.

Open Used_cars_classification.ipynb in Jupyter or Google Colab.

Run all cells to explore EDA, training, and results.



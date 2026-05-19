# 🎮 League of Legends — Win Rate Analysis

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> **Can we predict which team wins a League of Legends match — using only the first 10 minutes of data?**

---

## 📌 Project Overview

This project analyzes **9,879 high-Diamond ranked matches** to find what early-game factors best predict the final winner.

| Item | Detail |
|------|--------|
| Dataset | High Diamond Ranked Games (10 min) |
| Rows | 9,879 matches |
| Features | 40 columns → 16 selected |
| Best Model | Logistic Regression |
| Accuracy | **72.1%** |
| ROC-AUC | **0.806** |

---

## 🔍 Key Findings

1. **Gold Difference is the #1 predictor** (importance: 0.205)
2. **XP Difference is #2** (importance: 0.163)
3. **First Blood gives +13.3% win rate boost** — 59.7% vs 46.4%
4. **Dragon & Herald matter — but less than economy**
5. **Kills are misleading** — gold lead overrides kill lead

---

## 🤖 ML Models

| Model | Accuracy | ROC-AUC |
|-------|----------|---------|
| Logistic Regression | **72.1%** | **0.806** |
| Random Forest | 71.7% | 0.798 |

---

## 🚀 How to Run

```bash
pip install streamlit
streamlit run app.py
```

---

## 📁 Project Structure

```
lol-win-predictor/
├── data/
│   └── high_diamond_ranked_10min.csv
├── notebooks/
│   └── lol_win_rate_analysis.ipynb
├── app.py
├── lr_model.pkl
├── scaler.pkl
├── feature_names.json
└── README.md
```

---

## 🛠️ Tech Stack

- **Python** — pandas, numpy, scikit-learn, matplotlib, seaborn
- **ML** — Logistic Regression, Random Forest
- **App** — Streamlit
- **Environment** — Google Colab

---

## 👤 Author

Made with ❤️ as a Data Analyst portfolio project.

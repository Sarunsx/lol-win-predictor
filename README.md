# 🎮 League of Legends Early-Game Win Predictor

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> **"Can we predict the winning team in a League of Legends match using only the first 10 minutes of data?"**

## 📌 Project Overview
In a MOBA game like League of Legends, the early-game phase is crucial for building momentum. This project analyzes **9,879 High-Diamond ranked matches** to identify which early-game factors (first 10 minutes) statistically drive victories. 

Beyond Exploratory Data Analysis (EDA), I developed a predictive Machine Learning model and deployed it as an interactive web application to calculate real-time win probabilities.

### Executive Summary
- **Dataset:** High Diamond Ranked Games (10 min)
- **Data Size:** 9,879 matches, initially 40 features (reduced to 16 key features)
- **Best Model:** Logistic Regression
- **Performance:** **72.1%** Accuracy, **0.806** ROC-AUC
- **Deployment:** Interactive Web App using Streamlit

---

## 🔍 Exploratory Data Analysis (EDA) & Key Insights

Contrary to popular belief, hunting for kills isn't the most effective strategy to secure a win. The data reveals the following insights:

### 1. Economy Over Kills (Gold is King)
- **Gold Difference** is the single strongest predictor of winning (Feature Importance Score: `0.205`), closely followed by **Experience Difference** (`0.163`).
- **Insight:** Teams that secure a Top-25% gold lead at the 10-minute mark have a staggering **~78% win rate**. Kills are merely a means to an end; converting kills into gold and map control is what truly wins games.

*(Insert `phase3_feature_importance.png` here)*

### 2. The First Blood Momentum
- Securing "First Blood" significantly increases a team's chances of winning. Teams with First Blood have a **59.7%** win rate, compared to a **46.4%** win rate for those without it (+13.3% advantage).

### 3. Objectives are Indicators, Not Guarantees
- Securing early objectives like Dragons and Heralds boosts the win rate to around 59.5% - 64.1%. However, their overall feature importance is relatively low compared to raw economic power (Gold & XP).
- **Insight:** Prioritize safe farming over risky objective contests. 

*(Insert `phase4_insights_chart.png` here)*

---

## 🤖 Predictive Modeling

I trained and evaluated two fundamental classification models:

| Model | Accuracy | ROC-AUC |
| :--- | :---: | :---: |
| **Logistic Regression** | **72.1%** | **0.806** |
| Random Forest Classifier | 71.7% | 0.798 |

**Why Logistic Regression?**
Despite Random Forest being a more complex ensemble model, the relationship between 10-minute stats (like Gold/XP difference) and the final outcome is highly linear. Logistic Regression generalized better without overfitting and is far more computationally efficient.

*(Insert `phase3_model_evaluation.png` here)*

---

## 🚀 Interactive Web App (Deployment)

To make these insights actionable for gamers and esports analysts, I deployed the trained Logistic Regression model via **Streamlit**. 

Users can input real-time match statistics at the 10-minute mark (e.g., Kills, Gold Difference, CS/Min) and instantly receive the calculated win probability for both the Blue and Red teams.

### How to Run the App Locally:
```bash
# 1. Clone this repository
git clone [https://github.com/YourUsername/lol-win-predictor.git](https://github.com/YourUsername/lol-win-predictor.git)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py

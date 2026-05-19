import streamlit as st
import pandas as pd
import pickle
import json

with open('lr_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('feature_names.json', 'r') as f:
    feature_names = json.load(f)

st.set_page_config(page_title="LoL Win Predictor", page_icon="🎮", layout="wide")
st.title("🎮 League of Legends — Win Predictor")
st.markdown("กรอก stats ของทั้งสองทีมที่ **10 นาที** แล้วดูว่าทีมไหนจะชนะ!")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔵 Blue Team")
    blue_kills        = st.slider("Kills", 0, 20, 5, key="bk")
    blue_deaths       = st.slider("Deaths", 0, 20, 3, key="bd")
    blue_assists      = st.slider("Assists", 0, 30, 6, key="ba")
    blue_gold_diff    = st.slider("Gold Diff", -5000, 5000, 500, key="bgd")
    blue_xp_diff      = st.slider("XP Diff", -5000, 5000, 300, key="bxd")
    blue_gold_per_min = st.slider("Gold/Min", 1500, 3000, 1900, key="bgm")
    blue_cs_per_min   = st.slider("CS/Min", 0.0, 10.0, 6.5, key="bcs")
    blue_first_blood  = st.radio("First Blood?", [1, 0], format_func=lambda x: "Yes" if x else "No", key="bfb")

with col2:
    st.subheader("🔴 Red Team")
    red_kills         = st.slider("Kills", 0, 20, 3, key="rk")
    red_deaths        = st.slider("Deaths", 0, 20, 5, key="rd")
    red_assists       = st.slider("Assists", 0, 30, 4, key="ra")
    red_gold_per_min  = st.slider("Gold/Min", 1500, 3000, 1800, key="rgm")
    red_cs_per_min    = st.slider("CS/Min", 0.0, 10.0, 6.0, key="rcs")
    red_wards_placed  = st.slider("Wards Placed", 0, 30, 10, key="rwp")
    red_elite_monsters = st.slider("Elite Monsters", 0, 3, 0, key="rem")
    red_first_blood   = 1 - blue_first_blood

st.divider()

if st.button("🔮 Predict!", use_container_width=True):
    input_dict = {feat: 0 for feat in feature_names}
    input_dict.update({
        "blueKills": blue_kills,
        "blueDeaths": blue_deaths,
        "blueAssists": blue_assists,
        "blueGoldDiff": blue_gold_diff,
        "blueExperienceDiff": blue_xp_diff,
        "blueGoldPerMin": blue_gold_per_min,
        "blueCSPerMin": blue_cs_per_min,
        "blueFirstBlood": blue_first_blood,
        "redKills": red_kills,
        "redDeaths": red_deaths,
        "redAssists": red_assists,
        "redGoldPerMin": red_gold_per_min,
        "redCSPerMin": red_cs_per_min,
        "redWardsPlaced": red_wards_placed,
        "redEliteMonsters": red_elite_monsters,
        "redFirstBlood": red_first_blood,
    })

    input_df = pd.DataFrame([input_dict])[feature_names]
    input_scaled = scaler.transform(input_df)
    proba = model.predict_proba(input_scaled)[0]

    blue_win_pct = proba[1] * 100
    red_win_pct  = proba[0] * 100

    st.subheader("📊 ผลการทำนาย")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"### 🔵 Blue Team")
        st.markdown(f"# {blue_win_pct:.1f}%")
    with c2:
        st.markdown(f"### 🔴 Red Team")
        st.markdown(f"# {red_win_pct:.1f}%")

    if blue_win_pct > 50:
        st.success(f"🔵 Blue Team จะชนะ! (ความมั่นใจ {blue_win_pct:.1f}%)")
    else:
        st.error(f"🔴 Red Team จะชนะ! (ความมั่นใจ {red_win_pct:.1f}%)")

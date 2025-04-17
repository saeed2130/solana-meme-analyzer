# Solana Meme Coin Analyzer - V3.0 (Trending Token Scanner)
# Author: ChatGPT + [User]

import requests
import streamlit as st

# ⛔ جایگزین کن با کلید API واقعی خودت از birdeye.so
BIRDEYE_API_KEY = "YOUR_BIRDEYE_API_KEY"

st.set_page_config(page_title="Solana Trending Meme Tokens", layout="wide")
st.title("🚀 میم‌کوین‌های ترند در سولانا")
st.markdown("آخرین توکن‌های محبوب سولانا و بررسی سریع برای ورود 🔍")

def get_trending_tokens():
    url = "https://public-api.birdeye.so/public/tokenlist?sort_by=volume_h24&sort_type=desc&limit=50"
    headers = {
        "X-API-KEY": BIRDEYE_API_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data.get('data', [])

def get_token_details(token_address):
    url = f"https://public-api.birdeye.so/public/token/{token_address}"
    headers = {
        "X-API-KEY": BIRDEYE_API_KEY


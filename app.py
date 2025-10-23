import streamlit as st
from modules import bazi, ziwei
from ai import divination_ai

# 命理AI系统 - 主程序
st.set_page_config(page_title="命理AI系统", page_icon="🔮", layout="wide")

st.title("🔮 命理AI系统")
st.write("結合古籍智慧與現代AI，為您提供全面命理分析")

# 側邊欄選擇
menu = st.sidebar.selectbox(
    "選擇命理系统",
    ["八字排盤", "紫微斗數", "AI綜合分析"]
)

if menu == "八字排盤":
    st.header("八字排盤")
    # TODO: 輸入資料
    
elif menu == "紫微斗數":
    st.header("紫微斗數")
    # TODO: 輸入資料
    
else:
    st.header("AI綜合分析")
    # TODO: AI分析

import streamlit as st
from modules import bazi, ziwei
from datetime import datetime, date

# 命理AI系统 - 主程序
st.set_page_config(page_title="命理AI系统", page_icon="🔮", layout="wide")

# 自定義CSS樣式
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stButton>button {
        background-color: #667eea;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #764ba2;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔮 命理AI系统")
st.write("結合古籍智慧與現代AI，為您提供全面命理分析")

# 側邊欄選擇
menu = st.sidebar.selectbox(
    "選擇命理系统",
    ["八字排盤", "紫微斗數", "易經占卜"]
)

if menu == "八字排盤":
    st.header("📅 八字排盤")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("基本資料")
        name = st.text_input("姓名", placeholder="請輸入姓名")
        gender = st.selectbox("性別", ["男", "女"])
        birth_date = st.date_input("出生日期", value=date(1990, 1, 1))
        
    with col2:
        st.subheader("出生時間")
        birth_time = st.time_input("出生時辰")
        location = st.text_input("出生地點", placeholder="例如：香港")
        
    if st.button("🔍 開始排盤", use_container_width=True):
        if name:
            with st.spinner("正在計算八字..."):
                # 調用八字計算模塊
                try:
                    result = bazi.calculate_bazi(
                        year=birth_date.year,
                        month=birth_date.month,
                        day=birth_date.day,
                        hour=birth_time.hour
                    )
                    
                    st.success("✅ 計算完成！")
                    
                    # 顯示結果
                    st.subheader(f"📊 {name} 的八字排盤結果")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        year_p = result.get('year_pillar', {})
                        st.metric("年柱", f"{year_p.get('stem', '')}{year_p.get('branch', '')}" if isinstance(year_p, dict) else str(year_p))                    with col2:
                        month_p = result.get('month_pillar', {})
                        st.metric("月柱", f"{month_p.get('stem', '')}{month_p.get('branch', '')}" if isinstance(month_p, dict) else str(month_p))                    with col3:
                        day_p = result.get('day_pillar', {})
                                            hour_p = result.get('hour_pillar', {})
                        st.metric("日柱", f"{day_p.get('stem', '')}{day_p.get('branch', '')}" if isinstance(day_p, dict) else str(day_p))                    with col4:
                        st.metric("時柱"f"{hour_p.get('stem', '')}{hour_p.get('branch', '')}" if isinstance(hour_p, dict) else str(hour_p))
                    
                    # 五行分析
                    st.subheader("🌟 五行分析")
                    elements = result.get('elements', {})
                    if elements:
                        cols = st.columns(5)
                        for i, (element, count) in enumerate(elements.items()):
                            with cols[i]:
                                st.metric(element, count)
                    
                    # 詳細解析
                    st.subheader("📖 命理解析")
                    st.info(result.get('analysis', '正在分析中...'))
                    
                except Exception as e:
                    st.error(f"❌ 計算出錯: {str(e)}")
                    st.info("💡 這是演示版本，完整功能正在開發中")
        else:
            st.warning("⚠️ 請輸入姓名")

elif menu == "紫微斗數":
    st.header("⭐ 紫微斗數")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("基本資料")
        name = st.text_input("姓名", placeholder="請輸入姓名", key="ziwei_name")
        gender = st.selectbox("性別", ["男", "女"], key="ziwei_gender")
        birth_date = st.date_input("出生日期", value=date(1990, 1, 1), key="ziwei_date")
        
    with col2:
        st.subheader("出生時間")
        birth_time = st.time_input("出生時辰", key="ziwei_time")
        calendar_type = st.selectbox("曆法", ["陽曆", "陰曆"])
        
    if st.button("🔍 開始排盤", use_container_width=True, key="ziwei_btn"):
        if name:
            with st.spinner("正在排紫微斗數命盤..."):
                try:
                    result = ziwei.calculate_ziwei(
                        year=birth_date.year,
                        month=birth_date.month,
                        day=birth_date.day,
                        hour=birth_time.hour,
                        gender=gender
                    )
                    
                    st.success("✅ 排盤完成！")
                    
                    st.subheader(f"🌟 {name} 的紫微斗數命盤")
                    
                    # 十二宮位
                    st.subheader("🏛️ 十二宮位")
                    palaces = result.get('palaces', {})
                    if palaces:
                        cols = st.columns(4)
                        for i, (palace, stars) in enumerate(palaces.items()):
                            with cols[i % 4]:
                                st.write(f"**{palace}**")
                                st.write(stars)
                    
                    # 主星分析
                    st.subheader("✨ 主星特質")
                    st.info(result.get('main_star_analysis', '正在分析中...'))
                    
                except Exception as e:
                    st.error(f"❌ 計算出錯: {str(e)}")
                    st.info("💡 這是演示版本，完整功能正在開發中")
        else:
            st.warning("⚠️ 請輸入姓名")

else:  # 易經占卜
    st.header("📿 易經占卜")
    
    st.subheader("💭 請默想您的問題")
    question = st.text_area("您想詢問什麼？", placeholder="請輸入您的問題...", height=100)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🎲 開始占卜", use_container_width=True):
            if question:
                with st.spinner("正在起卦..."):
                    import time
                    time.sleep(1)
                    
                    # 模擬卦象
                    hexagrams = ["乾", "坤", "震", "巽", "坎", "離", "艮", "兌"]
                    import random
                    upper = random.choice(hexagrams)
                    lower = random.choice(hexagrams)
                    
                    st.success("✅ 占卜完成！")
                    
                    st.subheader(f"📊 卦象：{upper}{lower}")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("上卦", upper)
                    with col2:
                        st.metric("下卦", lower)
                    
                    st.subheader("📖 卦辭解析")
                    st.info(f"您問：{question}\n\n根據{upper}{lower}卦，建議您...（完整解析功能開發中）")
                    
                    st.subheader("💡 建議")
                    st.write("• 保持平常心\n• 順其自然\n• 積極面對")
            else:
                st.warning("⚠️ 請輸入您的問題")

# 頁腳
st.markdown("---")
st.caption("💫 命理AI系统 v1.0 | 結合古籍智慧與現代AI技術")

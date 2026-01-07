import streamlit as st
import pandas as pd

st.title("📅 학사 일정")

data = {
    "월": ["3월", "4월", "5월", "6월", "7월"],
    "일정": ["입학식 및 개학", "중간고사", "현장체험학습", "기말고사", "여름방학식"]
}
df = pd.DataFrame(data)

st.table(df) # 깔끔한 표 형태로 출력

st.info("※ 위 일정은 학교 사정에 따라 변경될 수 있습니다.")

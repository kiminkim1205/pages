import streamlit as st

st.set_page_config(page_title="우리학교 공식 홈페이지", layout="wide")

st.title("🏫 우리학교 홈페이지에 오신 것을 환영합니다")

# 배너 이미지 (학교 사진 URL이 있다면 대체하세요)
st.image("https://via.placeholder.com/800x400.png?text=Welcome+to+Our+School", use_column_width=True)

col1, col2 = st.columns(2)

with col1:
    st.header("📢 공지사항")
    st.write("- 2026학년도 신입생 모집 요강 안내")
    st.write("- 이번 주 금요일 동아리 발표회 개최")
    st.write("- 학교 급식 모니터링 요원 모집")

with col2:
    st.header("🌟 오늘의 한마디")
    st.info("“꿈을 향해 도전하는 사람이 되자.”")
    st.metric(label="현재 재학생 수", value="1,240명", delta="12명 증가")

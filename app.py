import streamlit as st
import pandas as pd

st.set_page_config(page_title="학생 이수시간 조회", page_icon="📘", layout="centered")

st.title("📘 학생 이수시간 조회 시스템")

st.write("이름과 생년월일을 입력하면 해당 학생의 정보를 확인할 수 있습니다.")


# 👉 여기에 구글 드라이브 파일 ID만 바꿔 넣으면 됨
FILE_ID = "1sfpSG3kTfFTRRldJkSHGkTrVFL9bRNUq"
URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"


@st.cache_data
def load_data():
    try:
        df = pd.read_excel(URL)
        return df
    except Exception as e:
        st.error("❌ 데이터를 불러오는 중 오류가 발생했습니다.\n\n"
                 "구글 드라이브 파일 공유 설정이 '링크가 있는 모든 사용자'인지 확인해주세요.")
        st.stop()


df = load_data()


# 입력 영역
st.subheader("🔍 학생 정보 입력")

name = st.text_input("이름")
birth = st.text_input("생년월일 (YYYYMMDD)", max_chars=8)


if st.button("조회하기"):
    if name.strip() == "" or birth.strip() == "":
        st.warning("⚠ 이름과 생년월일을 모두 입력해주세요.")
    else:
        # 검색
        result = df[(df["이름"] == name) & (df["생년월일"].astype(str) == birth)]

        if len(result) == 0:
            st.error("❌ 해당 학생을 찾을 수 없습니다.")
        else:
            st.success("✅ 조회 성공!")
            st.write("아래는 조회된 학생 정보입니다:")
            st.dataframe(result, use_container_width=True)

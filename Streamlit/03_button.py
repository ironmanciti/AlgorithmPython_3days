import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

# 앱의 제목을 설정합니다.
st.title("DataFrame 다운로드하기")

# CSV 파일을 읽어서 DataFrame 객체로 변환합니다.
df = pd.read_csv('winequality-red.csv', sep=";")

# 앱에서 DataFrame을 출력합니다. use_container_width=False는
# DataFrame의 너비가 컨테이너의 너비를 따르지 않도록 설정합니다.
st.dataframe(df, use_container_width=False)

# 사용자가 파일 이름을 입력할 수 있게 합니다.
file_name = st.text_input('다운로드할 파일 이름을 입력하세요:', 'winequality-red.csv')

# 입력받은 이름으로 파일을 다운로드 할 수 있는 버튼을 추가합니다.
csv = df.to_csv(index=False)  # DataFrame을 CSV 문자열로 변환합니다.
st.download_button(
    label="Download CSV",
    data=csv,
    file_name=file_name,
    mime='text/csv',
)

# checkbox
agree = st.checkbox("동의")
if agree:  # checkbox가 클릭된 경우
    st.write("동의하셨습니다.:100:")
    
# radio button
genre = st.radio("좋아하는 음식은?", ["스테이크", "피자", "햄버거"])
if genre == "스테이크":
    st.write("저도 좋아합니다.")
else:
    st.write(f"{genre}를 좋아하시는군요.")
    
# select box    
genre = st.selectbox("좋아하는 음식은?", ["없음", "피자", "햄버거"], index=0)
if genre == "없음":
    st.write("하나를 골라 주세요.")
else:
    st.write(f"{genre}를 좋아하시는군요.")
    
# 슬라이더
values = st.slider("숫자를 선택하세요.", 0, 100, (25, 75))
st.write(values)

# 숫자 입력
number = st.number_input(label="숫자를 입력하세요.", 
                         min_value=0, max_value=100, value=50)
st.write(number)
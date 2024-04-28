import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

#button click
button = st.button("버튼 클릭")
if button:
    st.write(":blue[버튼]이 클릭되었습니다.:sparkles:")
    
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

#download button
st.download_button(label="Download", data=df.to_csv(), file_name="data.csv", mime="text/csv")

# checkbox
agree = st.checkbox("동의")
if agree:
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

# 텍스트 입력
title = st.text_input(label="제목을 입력하세요.", 
                      placeholder="기본값")
st.write(title)

# 숫자 입력
number = st.number_input(label="숫자를 입력하세요.", 
                         min_value=0, max_value=100, value=50)
st.write(number)
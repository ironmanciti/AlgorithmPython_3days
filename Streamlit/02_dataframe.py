import streamlit as st
import pandas as pd
import numpy as np

st.title("DataFrame 출력하기")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# 앱에서 DataFrame을 출력. use_container_width=False는
# DataFrame의 너비가 컨테이너의 너비를 따르지 않도록 설정
st.dataframe(df, use_container_width=False)

# DataFrame을 테이블 형태로 앱에 고정하여 출력
st.table(df)

# 메트릭을 행단위로 표시
# 온도를 나타내는 메트릭을 설정. 현재 값과 변동량(델타)을 포함합니다.
st.metric(label="온도", value="30도", delta="1.2도") 
# 삼성전자 주식 가격을 나타내는 메트릭을 설정. 가격과 가격 변동량을 표시합니다. 
st.metric(label="삼성전자", value="61,000원", delta="-1,000원")  

# 메트릭을 열단위로 표시
col1, col2 = st.columns(2)  # 두 개의 열을 생성
# 첫 번째 열에 온도 메트릭을 표시
col1.metric(label="온도", value="30도", delta="1.2도")  
# 두 번째 열에 삼성전자 주식 가격 메트릭을 표시
col2.metric(label="삼성전자", value="61,000원", delta="-1,000원")  


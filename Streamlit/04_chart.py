import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({
    '이름': ['홍길동', '이순신', '강감찬', '김유신', '유관순'],
    '나이': [22, 31, 25, 40, 60],
    '몸무게': [75.5, 80.2, 55.3, 78.3, 45.5],
})

st.dataframe(df, use_container_width=True)

fig, ax = plt.subplots()
ax.bar(df['이름'], df['나이'])
st.pyplot(fig)

barplot = sns.barplot(data=df, x='이름', y='나이', palette='Set2')
fig = barplot.get_figure()
st.pyplot(fig)
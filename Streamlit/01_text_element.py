import streamlit as st

# 타이틀 적용 
st.title("이것은 타이틀입니다.")

# 이모지 이용
st.title("스마일:sunglasses:")
st.header("헤더:sparkles:")
st.subheader("서브헤더:star:")
st.caption("캡션:star2:")
st.text("단순히 text 출력")

#마크다운 출력 
st.markdown("공식은:green[$:\sum_{i=1}^{n}x_i$]이고 정답은 :red[100] 입니다.")
st.latex(r"Y = \alpha + \beta X_i")

# sample code 표시
sample_code = """
def function():
    print("Hello Streamlit!")
"""
st.code(sample_code, language="python")

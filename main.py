import streamlit as st
import random

# 초기 데이터 설정
names = ['김예진', '김종진', '문찬우', '오승옥', '유준선', '이윤이', '임세은']
people_num = 7
liar = 1
not_liar = people_num - liar

# 랜덤으로 선택된 사람 설정
selected_names = random.sample(names, 2)

# liar와 not_liar 리스트 생성
items = [selected_names[0]] * not_liar + [str(selected_names[1])+'(라이어입니다!)'] * liar
random.shuffle(items)

# 번호와 이름 추가
items = [f"{i+1}: {item}" for i, item in enumerate(items)]

# 미리보기 방지
items = [item for pair in zip(items, ["다음"] * len(items)) for item in pair][:-1]
items.insert(0, "시작!")
items.append('끝~')

# Session State 초기화
if "my_items" not in st.session_state:
    st.session_state.my_items = items  # 리스트 초기화
    st.session_state.index = 0  # 현재 보여줄 항목의 인덱스 초기화

# 현재 항목 출력
if st.session_state.index < len(st.session_state.my_items):
    st.write(f"{st.session_state.my_items[st.session_state.index]}")
else:
    st.write("모든 항목을 다 보셨습니다!")

# 버튼 클릭 시 다음 항목으로 이동
if st.button("다음 항목 보기"):
    if st.session_state.index < len(st.session_state.my_items) - 1:
        st.session_state.index += 1  # 인덱스 증가
    else:
        st.session_state.index = 0  # 모든 항목을 본 후 처음으로 돌아감
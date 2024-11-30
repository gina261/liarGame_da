import streamlit as st
import random


# 초기 데이터 설정
names = ['김민서', '김예진', '김종진', '문찬우', '서지연', '오승옥', '유준선', '이윤이', '임세은']
people_num = 9
liar = 2
not_liar = people_num - liar

# 랜덤으로 선택된 사람 설정
selected_names = random.sample(names, 2)

# liar와 not_liar 리스트 생성
items = [selected_names[0]] * not_liar + [selected_names[1]] * liar
random.shuffle(items)

# 번호와 이름 추가
items = [f"{i+1}: {item}" for i, item in enumerate(items)]

# Session State에 리스트 저장
if "my_items" not in st.session_state:
    st.session_state.my_items = items  # 최초 초기화

# 현재 리스트 출력
st.write("아이템 리스트:")
for item in st.session_state.my_items:
    st.write(item)
    
# 새로고침용 버튼
if st.button("리스트 재생성"):
    selected_names = random.sample(names, 2)
    items = [selected_names[0]] * not_liar + [selected_names[1]] * liar
    random.shuffle(items)
    st.session_state.my_items = [f"{i+1}: {item}" for i, item in enumerate(items)]

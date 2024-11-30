import random

names = ['김민서', '김예진', '김종진', '문찬우', '서지연', '오승옥', '유준선', '이윤이', '임세은']
people_num = 9
liar = 2
not_liar = people_num - liar

selected_names = random.sample(names, 2)

new_list = [selected_names[0]] * not_liar + [selected_names[1]] * liar

random.shuffle(new_list)

for i in range(len(new_list)):
    input()
    print(new_list[i])
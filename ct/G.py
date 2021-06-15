"""
monster 要喝水
Description

公司终于安好饮水机了，monster 迫不及待要去接水，但是他到那里才发现前面已经有n个同事了。他数了数，饮水机一共有m个接水口。所有的同事严格按照先来后到去接水（m个接水口同时工作，哪个水龙头有空人们就去哪里，如果 n \lt mn<m，那么就只有n个接水口工作）。每个人都有一个接水的时间，当一个人接完水后，另一个人马上去接，不会浪费时间。monster 着急要开会，所以他想知道什么时候才能轮到他。


Input
第一行两个整数n和m，表示 monster 前面有n个人，饮水机有m个接水口。n, m < 1100。第二行n个整数，表示每个同学的接水时间。


Output
一行，一个数，表示轮到 monster 接水的时间

"""
"""
4 2
1 1 1 1
"""
"""
3
"""

# io

water_machine_ls = [0, 0]
people_ls = [1, 1, 1, 1]
pos_cnt = len(water_machine_ls)
time_ = 0
flag = True
# flag 为空，可以进人，进人数量 > 前面人数的时候，停止计时
# 进人之后，加时间
out_cnt = len(people_ls)
people_cnt = 0
next_idx = 0
# while True:


# while next_idx < len(people_ls):
#     while pos_cnt > 0:
#         out_cnt -= 1
#         pos_cnt -= 1
#         time_ += people_ls[next_idx]
#         next_idx += 1
#         if pos_cnt == 0:
#             flag = False










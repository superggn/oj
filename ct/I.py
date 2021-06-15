"""
Description

斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，斐波那契数列以如下被以递推的方法定义

F(1)=1F(1)=1
F(2)=1F(2)=1
F(n)=F(n-1)+F(n-2)
其中 n≥3,n∈N∗
在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用。

请编程实现 F(n)F(n) 函数


Input
一列正整数n， 由换行符分隔开；


Output
斐波那契函数F(n)F(n)的计算结果，由换行符隔开

"""
"""
1
2
3
4
5
6
"""
"""
1
1
2
3
5
8
"""

def fib(n):
    if n <= 2:
        return 1
    a = 1
    b = 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


while True:
    str_in = input()
    if not str_in:
        break
    num = int(str_in)
    res = fib(num)
    print(res)

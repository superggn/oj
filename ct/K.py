"""
作为一家业内技术领先的公司，C 公司一直努力为企业客户提供高质量的产品和服务。

然而天有不测风云，由于某位程序员同学的一个 typo，C 公司核心产品在最新版中引入了一个 bug，于是在新版本对外发布的第二天早上，负责技术支持的 P 同学发现手机上收到了很多家客户的反(吐)馈(槽)，在快速了解清楚原因之后，P 同学决定马上派出技术支持同学们到各个客户现场处理问题。由于每家客户的环境复杂程度不同，以及工作经验原因每位技术支持同学处理问题的能力也不同，P 同学冷静的分析了一下目前的状态：

一共有 N 家客户遇到了问题，第 i 家客户需要能力值达到p[i]的技术支持同学才能解决问题；

一共有 K 位技术支持同学，第 i 位技术支持同学的能力值为w[i]；

由于问题比较复杂，每位技术支持同学当天只能处理一家客户的问题；

每家客户最多只能派一位技术支持同学

P 同学希望当天能处理尽可能多家客户，聪明的你能告诉他当天最多有几家客户的问题能得到处理吗？


Input
第一行输入一个整数 T，代表数据组数，对于每组数据：

第一行输入两个整数 N (1 ≤ N ≤ 10) 和 K (1 ≤ K ≤ 10)，表示出问题的客户数量和技术支持同学的人数；

第二行输入输入 N 个整数，第 i 个整数表示第 i 家客户对能力值的需求；

第三行输入 K 个整数，第 i 个整数表示第 i 位技术支持同学的能力值。


Output

对于每组输入，输出一个整数 R，表示当天最多有 R 家客户的问题能得到处理。

"""
"""
2
3 3
5 7 9
6 8 10
3 5
5 7 9
3 3 5 3 3

"""
"""
3
1
"""


def ls_str_2_int(str_ls):
    for idx in range(len(str_ls)):
        str_ls[idx] = int(str_ls[idx])
    return


def find_solution_num(num_ls_, client_ls_, staff_ls_):
    client_ls_.sort()
    staff_ls_.sort()
    idx_c = len(client_ls_) - 1
    idx_s = 0
    cnt = 0
    while idx_c >= 0:
        # client 从右向左走
        # staff 从左向右走
        if staff_ls_[idx_s] >= client_ls_[idx_c]:
            cnt += 1
            staff_ls_[idx_s] *= -1
            idx_s = 0
            idx_c -= 1
        else:
            idx_s += 1
            if idx_s >= len(staff_ls_):
                idx_c -= 1
                idx_s = 0
    return cnt


case_num = int(input())
for _ in range(case_num):
    num_ls = input().split()
    client_ls = input().split()
    staff_ls = input().split()
    ls_str_2_int(num_ls)
    ls_str_2_int(client_ls)
    ls_str_2_int(staff_ls)
    print(find_solution_num(num_ls, client_ls, staff_ls))





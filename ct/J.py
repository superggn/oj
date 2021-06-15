"""
Description

在一次渗透特别行动中，由于一个特别的隧道只能传递 0-9A-Z 这 36 个字符（注意：全部大写），聪明的你决定发明 36 进制来解决数据传输问题。

在 36 进制表达方案中，0 仍然代表 0，9 也依然代表 9，A 代表 10，B 代表 11，依次类推，Z 代表 35。

与常见 10 进制书写方法类似（如：123 这个数字，1代表百位，是最大的一位），你发明的 36 进制编码也是按照最大的位放在最左边来输出的。

题目任务：给定一个 base64 字符串，将这个 base64 所编码的原始内容转换成 36 进制并输出。

提示：首先需要将 base64 字符串解码得到原始内容，然后将原始内容转换成 36 进制的最短表达。

提示2：仔细观察样例输入输出，确保弄明白编码的方式。


Input
一个字符串，确保是符合 base64 格式的字符串。


Output

编码为 36 进制的最终结果。


"""
"""
YQ==
    a
eW8=
    yo
cGFzc3dvcmQgaXMgQWRtaW4xMjM0NTY=
"""

"""
2P
    2   
    97
NZJ
    23  35  19
    
3N4I4HGY6IPFI151WM1CU9FGSRJ8QLQSL92U
"""

"""
base64 -> binary

binary -> base36
"""

import base64


def get_36_base_char(num):
    if num < 10:
        return str(num)
    return chr(ord("A") + num - 10)


def base_convert_36(str_in_):
    num_base = 36
    bin_str_ls = []
    for character in str_in_:
        cur_bin_str = bin(ord(character)).split('b')[-1].rjust(8, '0')
        bin_str_ls.append(cur_bin_str)
    bin_str = "".join(bin_str_ls)
    dec_num = int(bin_str, 2)
    res = []
    while dec_num != 0:
        cur_position_num = dec_num % num_base
        dec_num //= num_base
        res.append(get_36_base_char(cur_position_num))
    res.reverse()
    return "".join(res)


str_in = input().strip()

raw_ascii = base64.b64decode(str_in.encode()).decode()

print(base_convert_36(raw_ascii))



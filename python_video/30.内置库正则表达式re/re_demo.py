# -*- coding: utf-8 -*-
# @Author : feier
# @File : re_demo.py
import re

# 匹配包含 hogwarts 的字符串
# pattern = r"hogwarts"

# 转换为正则对象
# prog = re.compile(pattern)

# 匹配以 hog 开头的字符串
# pattern = r"hog\w+"

# s1 = "Hogwarts is a magic school"
# match1 = re.match(pattern, s1, re.I)
# match1 = re.search(pattern, s1, re.I)
# print(match1)
# print(f"匹配值的起始位置为：{match1.start()}")
# print(f"匹配值的结束位置为：{match1.end()}")
# print(f"匹配位置的元组为：{match1.span()}")
# print(f"要匹配的字符串为：{match1.string}")
# print(f"匹配的数据为：{match1.group()}")
# match_list1 = re.findall(pattern, s1, re.I)
# print(match_list1)

# s2 = "I like hogwarts hogwarts"
# match2 = re.match(pattern, s2, re.I)
# match2 = re.search(pattern, s2, re.I)
# print(match2)
# match_list2 = re.findall(pattern, s2, re.I)
# print(match_list2)

# 匹配手机号码
pattern = r"1[34578]\d{9}"

s1 = "中奖号码 123456，联系电话 15611111111"
result = re.sub(pattern, '1xxxxxxxxxx', s1)
print(result)

p = r"[?|&]"

url = "https://www.baidu.com/s?wd=%E9%9C%8D%E6%A0%BC%E6%B2%83%E5%85%B9%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91&rsv_spt=1&rsv_iqid=0xdc2997e0000adc07&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&rsv_sug2=0&rsv_btype=i&inputT=6346&rsv_sug4=6712"

r = re.split(p, url)
print(r)
"""
    1、关键点一：每行的长度不超过一百个单位，且元素不能分别存储在两行
    2、关键点二：每一个元素对应需要的单位数由数组widths给出
    3、使用python中的ord()函数获取当前字符在字母表中的位置顺序
    4、while循环中的ch_num方法是此方法的核心点，重置计算基数
"""

def numberOfLiines(widths, s):
    width_Max = 100
    line = 1
    ch_num = 0
    for i in s:
        ch_num += widths[ord(i) - ord('a')]
        while ch_num > width_Max:
            line += 1
            ch_num = widths[ord(i) - ord('a')]   # 这一步没想到,最关键的一步，在此步把ch_num重置了
    return [line, ch_num]


widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"

result = numberOfLiines(widths, s)
print(result)
"""
题目：
设定一种五进制数值的表示方式，他的美以数位可能是字母o,y,e,a,s其中的一个，分别代表
数字0，1，2，3，4。例如，五进制数ya对应的十进制数为8，无尽之树对应的ysoae对应的十
进制树为1142，现在给定一个五进制数，输出对应的十进制数，或给定一个十进制数，输出它
的对应的五进制数
"""

"""
输入描述：
    第一行是一个正整数T(T<=100),表示测试数据的数组，接下来是每一组测试数据。
    每组测试数据只有一行，为一个五进制正整数或十进制正整数，该整数的值不超过1e9.
"""
"""
输出描述：
    每组测试数据输出一行，如果输入为五进制整数，则输出它对应的十进制整数；如果输入为
    十进制整数，则输出它对应的五进制整数。
"""

data = "oyeas"
dict = {
    "o":"0",
    "y":"1",
    "e":"2",
    "a":"3",
    "s":"4",
    "0":"o",
    "1":"y",
    "2":"e",
    "3":"a",
    "4":"s"
}

# 数据输入函数
def inPut():
    while True:
        x = input()
        count = 0
        for i in x:
            if i not in data:
                print("输入不合法")
                break
            count += 1
        if len(x) == count:
            break
    while True:
        y = input()
        count = 0
        for i in y:
            if i not in data:
                print("输入不合法")
                break
            count += 1
        if len(y) == count:
            break
    return x,y

# 10进制转换5进制
def f_5(n):
    int_b, float_b = "", ""
    int_n = eval(str(n).partition(".")[0])
    float_n = 0
    if str(n).partition(".")[2] != "":
        float_n = eval("0."+str(n).partition(".")[2])
    while True:
        s = int_n/5
        y = int_n%5
        int_b += str(y)
        if s==0:
            break
        int_n=s
    if str(n).partition(".")[2] != "":
        for i in range(5):
            s = float_n*5
            if(s!=0):
                float_b+=str(s).partition(".")[0]
            else:
                break
            float_n = eval("0."+str(s).partition(".")[2])
    return int_b[::-1]+"."+float_b


#5进制转换10进制
def f_10(x):
    s_x= ""
    n = 0
    for i in range(len(x)):
        s_x += dict[x[i]]
    if s_x.partition(".")[2] != "":
        numx = int(s_x.partition(".")[0],5)
        s = s_x.partition(".")[2]
        for i in range(len(s)):
            n += eval(s[i])*(5**(-(i+1)))
    else:
        numx = eval(str(int(s_x.partition(".")[0],5)))
#     print(numx+n)
    return numx+n

if __name__=="__main__":
    while True:
        n = input("请输入选项：")
        if n=="1":
            x,y = inPut()
            numx,numy = f_10(x),f_10(y)
        elif n=="2":
            x,y = inPut()
            numx,numy = f_10(x),f_10(y)
        elif n=="3":
            x,y = inPut()
            numx,numy = f_10(x),f_10(y)
        elif n=="0":
            break
        else:
            print("输入错误！")

"""
题目：深信服每年都会组织员工旅游。旅游由各部门自行组织，部门中每个人都有一个方便旅游的时间段。
现在部门有要组织旅游了，助理收集了每个人觉得方便的时间段，要决定一个旅游时间段，目标是让尽可能多的员工觉得方便。
请计算最多可以让多少人觉得方便。
"""
"""
输入描述：
第一行为一个正整数T,表示测试书觉得组数。T<=100.
接下来是每组测试数据：
    每组测试数据的第一行是一个正整数N(N<=100000),表示共有多少名员工。
    接下来是N行，每行表示一个员工的方便时间段，用两个正整数A、B表示(A<=B<=1000000).
    例如A为5,B为8,表示该员工在5、6、7、8这四个时间点旅游都是方便的。

输出描述：
每组测试数据输出一行，为一个整数，表示最多可以让多少人觉得方便
"""
# 声明有三组数据
T = int(input())
while True:
    l = [input()]
    if len(l) == 1:
        list1 = []
        for i in range(int(l[0])):
            list1.append(list(map(int, input().strip().split(" "))))
        # list1.sort(key=lambda x:(x[0], x[1]))
        list1.sort()
        ans = 1
        maxCount = 1
        list2 = []
        for i in list1:
            if not list2 or list2[-1][1] < i[0]:
                list2.append(i)
                ans = 1
            else:
                list2[-1][1] = min(list2[-1][1], i[1])
                list2[-1][0] = max(list2[-1][0], i[0])
                ans += 1
            maxCount = max(maxCount, ans)
        print(maxCount)

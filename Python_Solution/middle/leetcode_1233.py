# 2023/2/8  author:WH

# author:WH 核心想法是排序之后进行元素对比
class Solution:
    def removeSubfolders(self, folder):
        folder.sort()
        # print(folder)
        ans = folder[:1]
        for i in folder[1:]:
            # print(ans[-1][:2])
            print(i[:len(ans[-1])])
            # 起初漏掉了此处if语句中的and部分
            if i[:len(ans[-1])] == ans[-1] and i[len(ans[-1]):len(ans[-1])+1] == '/':
                continue
            else:
                # print(i)
                ans.append(i)
        return ans

if __name__ == "__main__":
    # folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    folder = ["/a/b/c","/a/b/ca","/a/b/d"]
    result = Solution().removeSubfolders(folder)
    print(result)



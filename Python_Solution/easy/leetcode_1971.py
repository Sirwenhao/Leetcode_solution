# 2022/12/19 author:github
# 并查集
class Solution:
    def validPath(self, n, edges, source, destination):
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        p = list(range(n))
        for u,v in edges:
            p[find(u)] = find(v)
        return find(source) == find(destination)

if __name__ == "__main__":
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    result = Solution().validPath(n, edges, source, destination)
    print(result)
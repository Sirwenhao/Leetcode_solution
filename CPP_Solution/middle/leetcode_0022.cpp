#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution{
    public:
    vector<string> genrateParenthesis(int n){
        vector<string> ans;
        function<void(int, int, string)> dfs = [&](int l, int r, string t){
            if (l > n || r > n || l < r) return;
            if(l == n && r == n){
                ans.push_back(t);
                return;
            }
            dfs(l+1, r, t+"(");
            def(l, r+1, t+")");
        };
        dfs(0, 0, "");
        return ans;
    }
};

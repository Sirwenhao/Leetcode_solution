// 2022/11/23  author:WH 组合总和
#include<iostream>
#include<vector>
#include<algorithm> //sort函数的使用
using namespace std;

class Solution{
private:
    vector<vector<int>> result;
    vector<int> path;
    void backtracking(vector<int>& candidates, int target, int sum, int startIndex){
        if (sum == target){
            result.push_back(path);
            return;
        }
        // 剪枝：如果sum+candidates[i] > target 就终止遍历
        for (int i = startIndex; i < candidates.size() && sum + candidates[i] <= target; i++){
            sum += candidates[i];
            path.push_back(candidates[i]);
            backtracking(candidates, target, sum, i);
            sum -= candidates[i];
            path.pop_back();
        }
}

public:
    vector<vector<int>> combinationsSum(vector<int>& candidates, int target){
        result.clear();
        path.clear();
        sort(candidates.begin(), candidates.end()); //对candidates排序
        backtracking(candidates, target, 0, 0);
        return result;
    }
/* 2023/7/14 author:WH */
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;

class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        vector<int> res(k);
        
        sort(arr.begin(), arr.end());
        for (int i = 0; i < k; ++i){
            res[i] = arr[i];
        }
        return res;
    }
}; 
int main(){
    int arr[3] = {3,2,1};
    int k = 2;
    Solution().getLeastNumbers(arr, k);
}

#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
    int search(vector<int>& nums, int target){
        int left = 0;
        int right = nums.size()-1;
        while(left <= right){
            int middle = left + ((left+right)/2);
            if(nums[middle] > target){
                right = middle-1;
            }
            else if(nums[middle] < target){
                left = middle + 1;
            }
            else{
                return middle;
            }
        }
        return -1;
    }


    int main(){
        nums = [1,2,3,4,5,6];
        target = 2;
        result = Solution().search(nums, target)
        cout << result << endl;
    }
}

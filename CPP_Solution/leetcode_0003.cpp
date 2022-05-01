#include<iostream>
using namespace std;
#include<map>

class Solution{
public:
    int lengthOfLongestSubstring(string s){
        int ans = 0, start = 0;
        int n = s.length();
        map<char, int> mp;

        for(int i=0; i<n; i++){
            char alpha=s[i];
            if(map.count(alpha)){
                start = max(start, mp[alpha]+1);
            }
            ans = max(ans, i-start+1);
            mp[alpha] = i;
        }
        return ans;
    }
};

int main()
{
    Solution().lengthOfLongestSubstring("abcabcbb");

    system("pause");

    return 0;
}
#include<iostream>
using namespace std;

class Solution{
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
        ListNode* ret = nullptr;
        ListNode* cur = nullptr;
        int carry = 0;
        while (l1 != nullptr || l2 != nullptr || carry != 0){
            carry += (l1 == nullptr ? 0 : l1->val) + (l2 == nullptr ? 0 : l2->val);
            auto temp = new ListNode(carry % 10);
            carry /= 10;
            if(ret == nullptr){
                ret = temp;
                cur = ret;
            }
            else{
                cur->next = temp;
                cur = cur->next;
            }
            l1 = l1 == nullptr ? nullptr : l1->next;
            l2 = l2 == nullptr ? nullptr : l2->next;
        }
        return ret;
    }
};
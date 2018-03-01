/*
思路：直接各位相加即可，要注意边界条件的判断。设置一个flag位用于表示进位。
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyHead = new ListNode(0);
        if (l1==NULL && l2==NULL){
            return dummyHead;
        }
        int sum = 0, flag = 0;
        ListNode* res = dummyHead;
        while(l1 || l2){
            int dig1 = l1?l1->val:0;
            int dig2 = l2?l2->val:0;
            sum = dig1 + dig2 + flag;
            res->next=new ListNode(sum%10);
            res = res->next;
            flag = sum/10;
            l1 = l1?l1->next:l1;
            l2 = l2?l2->next:l2;
        }
        if (flag!=0){
            res->next = new ListNode(flag);
        }
        return dummyHead->next;
    }
};

/*
思路：分别计算得到链表A和B的长度lenA和lenB.对于较长的链表，使其向后移动|lenA-lenB|的距离，最后设定两个指针逐一比较即可。
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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB)
            return NULL;
        int lenA = getLength(headA), lenB = getLength(headB);
        if(lenA>lenB){
            for (int i=0;i<(lenA-lenB);i++){
                headA = headA->next;
            }
        }
        if(lenA<lenB){
            for (int i=0;i<(lenB-lenA);i++){
                headB = headB->next;
            }
        }
        
        while(headA!=headB && headA && headB){
            headA = headA->next;
            headB = headB->next;
        }
        return headA==headB?headA:NULL;
    }
private:
    int getLength(ListNode *head){
        int count=0;
        while(head){
            count++;
            head=head->next;
        }
        return count;
    }
};

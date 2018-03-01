/*
思路：设置low和high分别用来表示递增三元组中的最小和中间的数。若当前数比下界low小，则更新下界（假设当前low取值为5，若存在递增三元组，说明剩下必然存在2个
数比5大；若此时元素为3，小于5，说明原来的2个数仍然比3大，还能增加寻找范围）；若当前数比low大比high小，则更新high；若当前数比low和high都要大，证明递增三
元组存在。
*/
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int low = INT_MAX, high = INT_MAX;
        for (int x : nums){
            if (x <= low){
                low = x;
            }
            else if (x <= high){
                high = x;
            }
            else{
                return true;
            }
        }
        return false;
    }
};

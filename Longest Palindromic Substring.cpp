/*
思路：回文数是按照中心某一个元素或是某两个元素对称的。因此只需遍历整个字符串s，设置两个指针，同时向两边扩展即可。需要注意的是要考虑一个元素对称和两个元素
对称这两种情况。
*/
class Solution {
    private: int low;
    private: int maxlen;
public:
    string longestPalindrome(string s) {
        int len = s.length();
        if (len<2) return s;
        for (int i=0;i<len;i++){
            extendPalindrome(s,i,i);
            extendPalindrome(s,i,i+1);
        }
        return s.substr(low,maxlen);
    }
private:
    void extendPalindrome(string s, int j, int k){
        while(j>=0&&k<s.length()&&s[j]==s[k]){
            j--;
            k++;
        }
        if (maxlen<k-j-1){
            low=j+1;
            maxlen=k-j-1;
        }
    }
};

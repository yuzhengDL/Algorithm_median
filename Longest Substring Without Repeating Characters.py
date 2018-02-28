/*
思路：滑动窗口法。使用字典记录字符最近出现的位置，如果遇到重复的字母，则更新左边界（即左边界向右移动一次），计算窗口滑动过程中的最大长度。
*/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        res = 0  
        left = 0  
        d = {}  
  
        for i, ch in enumerate(s):  
            if ch in d and d[ch] >= left:  
                left = d[ch] + 1  
            d[ch] = i  
            res = max(res, i - left + 1)  
        return res 

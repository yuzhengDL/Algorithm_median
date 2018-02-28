/*
思路：利用哈希表，将列表中的每一个元素转换成哈希表特征；然后通过构建字典的方式得到group
*/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        group = collections.defaultdict(list)
        for str in strs:
            counter = [0] * 26
            for char in str:
                counter[ord(char) - ord('a')] += 1
            group[tuple(counter)].append(str)
        return group.values()

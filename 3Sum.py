/*
思路：和twosum的思路相似，这里我们可以把第三个数-c作为target，然后调用twosum的算法即可（先排序，再设定以前一后两个指针）。这里要注意对于重复解的判断，
即遇到相同的target直接跳过。
*/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i==0 or nums[i]!=nums[i-1]:
                front, last = i + 1 
                last = len(nums)-1
                while front < last:
                    if nums[front]+nums[last] == -nums[i]:
                        res.append([nums[front],nums[last],nums[i]])
                        front += 1; last -= 1
                        while front < last and nums[front]==nums[front-1]:
                            front += 1
                        while front < last and nums[last]==nums[last+1]:
                            last -= 1
                    elif nums[front]+nums[last] < -nums[i]:
                            front += 1
                    else:
                            last -= 1
        return res

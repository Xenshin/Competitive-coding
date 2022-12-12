class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = []
        sums = []
        for i in range(len(nums)):
            temp.append(nums[i])
            sums.append(sum(temp))
        return sums
        
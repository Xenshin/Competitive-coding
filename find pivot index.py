class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftS = 0
        rightS = sum(nums)
        for i in range(len(nums)):
            rightS -= nums[i]
            if leftS == rightS:
                return i
            leftS += nums[i] # doubt ??
        return -1 
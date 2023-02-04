import sys
sys.stdout = open('CP\output.txt', 'w')
sys.stdin = open('CP\input.txt', 'r')

# Write your code here
def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                elif nums[i] + nums[j] == target:
                    return (i,j)
        return None
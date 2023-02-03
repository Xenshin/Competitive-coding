nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        elif nums[i]+nums[j] == target:
            return(i,j)
        else:
            return -1
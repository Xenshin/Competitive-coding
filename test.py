nums = [1,7,3,6,5,6]
for i in range(1,len(nums)-1):
    lsum = sum(nums[:i])
    rsum = sum(nums[i+1:])
    if lsum == rsum:
        print(i)
        
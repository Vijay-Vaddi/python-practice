#leetcode 153 find the minimum in rotated sorted array

nums = [4,5,6,7,0,1,2]

res = nums[0]
l, r = 0, len(nums)-1

while l<=r:
    if nums[l]<nums[r]:
        res = min(res, nums[l])
        break
    mid = (l+r)//2
    res = min(res,nums[mid])
    
    if nums[mid]>=nums[l]:
        l = mid+1
    else:
        r = mid-1
    
print(res)




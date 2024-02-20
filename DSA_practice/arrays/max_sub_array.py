# 53. Maximum Subarray
# Given an integer array nums, find the subarray
#  with the largest sum, and return its sum.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Brute force. 

nums = [-2,1,-3,4,-1,2,1,-5,4]

res = nums[0]
for i in range(len(nums)):
    
    max_sub=nums[i]
    sum = nums[i]
    for j in range(i+1, len(nums)):
        sum = sum+nums[j]
        
        max_sub = max(max_sub, sum)
       
    res = max(max_sub, res)

print(res)
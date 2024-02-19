# 189 leetcode
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

nums = [1,2,3,4,5,6,7]
k=3

def rotate(nums,k):
    for k in range(k):
        print('inside')
        nums.insert(0,nums[-1])
        nums.pop()
        
    print(nums)
    return nums

def split_and_rotate(nums, k):

    if k>len(nums):
        k = k%len(nums)
    
    first_elems = nums[:-k] #start from the beginning but end at excluding last k elems/count
    last_elems = nums[-k:] #start from the k count FROM THE END and go till the end

    nums[:] = last_elems+first_elems    
    return nums

print(rotate(nums, k))
print(split_and_rotate(nums, k))


# 283. Move Zeroes
'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0] '''

nums = [0,1,0,3,12]
ln = len(nums)
i=0
j=0
while i<ln:

    if nums[j] == 0:
        del nums[j]
        nums.append(0)
    else:
        j=j+1
    
    i=i+1

print(nums)

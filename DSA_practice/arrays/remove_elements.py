'''27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).'''

nums = [0,1,2,2,3,0,4,2]
# nums = [3,2,2,3]
val = 2

def plain_brute(nums, val):
    k = 0
    i = 0 
    while i< len(nums):
        if nums[i] == val:
            del nums[i]
        else:
            k = k+1
            i=i+1
    return k

def using_for(nums, val): 
    index = 0 
    for i in range(len(nums)):
        if nums[i] == val:
            continue
        else:
            nums[index] = nums[i]
            index+=1
    return index

def using_while(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)


print(plain_brute(nums, val),' ', using_for(nums, val),' ',using_while(nums, val) )
        

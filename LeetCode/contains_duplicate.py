# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Input: nums = [1,2,3,1]
# Output: true


nums = [1,2,3,4]
res = set()
def contains_duplicate(nums):
    for num in nums:
        if num not in res:
            res.add(num)
        elif num in res:
            return True
    return False    

print(contains_duplicate(nums))
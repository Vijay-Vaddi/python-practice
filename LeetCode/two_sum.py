# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# save the difference in a dict

nums = [2,7,11,15] 
target = 13


def two_sum(nums, target):
    diff_dict = {}
    for i, num  in enumerate(nums):
        diff = target-num
        
        if diff not in diff_dict:
            diff_dict[num] = i
        else: 
            print(diff_dict.items())
            return [diff_dict[diff], i]

print(two_sum(nums, target))
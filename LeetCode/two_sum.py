# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# save num and its index in a dict, if target-num is in dict as keys, 
# i,e one of the nums, return its and that nums index. 

nums = [2,7,11,15] 
target = 26


def two_sum(nums, target):
    num_index_dict = {}
    for i, num  in enumerate(nums):
        diff = target-num
        
        if diff not in num_index_dict:
            num_index_dict[num] = i
        else: 
            print(num_index_dict.values())
            return [num_index_dict[diff], i]

print(two_sum(nums, target))
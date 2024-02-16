# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# save num and its index in a dict, if target-num is in dict as keys, 
# i,e one of the nums, return its and that nums index. 

nums = [2,-7,-15,15,15,11,15] 
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

def two_sum_yes_no(nums, target):
    set1 = set()
    for num in nums:
        
        if target-num in set1:
            return True
        else:
            set1.add(target-num)
    return False        

print(two_sum(nums, 0))
print(two_sum_yes_no(nums, 0))
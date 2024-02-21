'''169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the arra
Example 1:
Input: nums = [3,2,3]
Output: 3'''
nums = [3,2,3]

def majorityElement(nums) -> int:
    
    dic = {}
    for i in nums:

        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
    
    return max(dic, key=dic.get)

print(majorityElement(nums))
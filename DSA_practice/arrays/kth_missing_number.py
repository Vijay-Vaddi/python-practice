''' 1539. Kth Missing Positive Number
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.'''

arr = [2,3,4,7,11]
# arr = [2] #5,6,7,8,9
k = 5
def bruto_force(arr, k):
    next_item = 0
    i = 0
    n = 0
    while n<k:

        # only till end of array
        if i<len(arr):
            # check if next item is in increment, if yes, make next item=current item
            if arr[i] == next_item+1:
                next_item = arr[i]
                i=i+1
            # else add it to array and count k
            else:   
                # items.append(current_item+1)
                n = n+1
                next_item = next_item+1
        else:
            # items.append(current_item+1)
            n=n+1
            next_item = next_item+1
    return next_item

def binary_sol(arr, k):

    l, r = 0, len(arr)-1

    while l<=r:

        mid = (l+r)//2
        missing_items = arr[mid] -(mid+1)

        if missing_items<k:
            l = mid+1
        else:
            r = mid-1
    
    return r+k+1

print(bruto_force(arr, k))
print(binary_sol(arr, k))



       


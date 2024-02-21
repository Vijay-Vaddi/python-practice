if item == nums[i]:
        count=count+1

    if count>2:
        nums.remove(item)
        nums.append('#')
        k=k+1

    if item!=nums[i]:
        item = nums[i]
     
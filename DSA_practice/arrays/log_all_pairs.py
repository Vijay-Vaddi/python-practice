list1 = [1,2,3,4,5]

for index, item in enumerate(list1):
    for j in range(len(list1)):
        print(item,'-',list1[j])

# for nested loops 
        # O(m*n) --> n^2 (n sqaured) if m==n. 
        # O(n^2) --> This is called quadratic time. 
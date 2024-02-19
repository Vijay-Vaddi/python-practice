list_a = [0, 3, 4, 7]
list_b = [0, 1, 3, 5, 8, 9]

new_list = sorted(list_a + list_b)

def while_sort(list1, list2):
    ln = len(list1)-1
    i,j = 0,0

    while i <=len(list1)-1:
    
        if list1[i] >= list2[j] and list1[i]<=list2[j+1]:
            list2.insert(j+1, list1[i])
            i=i+1
            ln = ln -1
            j=0
        else:
            j=j+1

    return list2

def merge_sort(list1, list2):
    merged = []
    i, j = 0,0

    while i<len(list1) and j < len(list2):
        if list1[i]< list2[j]:
            merged.append(list1[i])
            i=i+1
        elif list1[i] > list2[j]:
            merged.append(list2[j])
            j=j+1
        else: 
            merged.append(list1[i])
            i=i+1
            j=j+1


    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


print(while_sort(list_a, list_b))    
print(merge_sort(list_a, list_b))            

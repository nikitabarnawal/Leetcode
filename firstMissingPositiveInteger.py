#Given an unsorted integer array, find the smallest missing positive integer.
#Example 1:

#Input: [1,2,0]
#Output: 3

#Example 2:

#Input: [3,4,-1,1]
#Output: 2

#Example 3:

#Input: [7,8,9,11,12]
#Output: 1

def missingInt(arr,n):
    min = 0
    for i in range(n):
        if arr[i] > 0:
            min = arr[i]
            break;

    if min == 0:
        return 1
    
    for i in range(n):
        if min > arr[i] and arr[i] > 0:
            min = arr[i]
    
    if min == 1:
        i = 0
        while(i<n):
            if min+1 == arr[i]:
                min = arr[i]
                i = 0
            else:
                i+= 1
        return min+1

    return 1



arr = [4,1,2,3]
n = len(arr)
print(missingInt(arr,n))

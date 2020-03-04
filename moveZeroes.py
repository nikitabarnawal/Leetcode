'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    check = False
    j = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            if not check:
                j = i
                check = True
            continue
        else:
            nums[j],nums[i] = nums[i],nums[j]
            j = j + 1
    return nums
                
    
nums = [0,1,0,3,12]
print(moveZeroes(nums))

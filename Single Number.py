'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

'''

def singleNumber(nums):
    mp = {}
        
    for i in nums:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
                
    for key,value in mp.items():
        if value == 1:
            return key


nums = [4,1,2,1,2]
print(singleNumber(nums))

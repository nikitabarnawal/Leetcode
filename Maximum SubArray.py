'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def maxSubArray(nums):
    sum = 0
    maxSum = nums[0]
    B = []
    C = []

    for i in nums:
        sum = sum + i
        B.append(i)

        if sum > maxSum:
            maxSum = sum
            C = B

        if sum < 0:
            sum = 0
            B = []

    return maxSum


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(arr))

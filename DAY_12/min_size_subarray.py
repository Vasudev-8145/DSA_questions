"""
Minimum size subarray

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

nums = [1,4,4]
target = 4

left = 0
curr_sum = 0
min_length = len(nums)+1

for right in range(0,len(nums)):

    curr_sum += nums[right]

    while curr_sum >= target:

        currr_length = right-left+1

        if currr_length < min_length:

            min_length = currr_length

        curr_sum -= nums[left]
        left+=1

if min_length == len(nums)+1:

    print(0)

else:

    print(min_length)

        

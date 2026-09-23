"""
move zeros

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
"""

nums = [0,1,0,3,12]

num_list = []
zero_list = []

for num in nums:

    if num > 0:

        num_list.append(num)

    elif num == 0:

        zero_list.append(num)

final_list = num_list+zero_list

print(final_list)
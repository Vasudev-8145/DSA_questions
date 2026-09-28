"""
Maximum average subarray

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""

nums = [5]
k = 1
avg = 0
i = 0
j = k

if len(nums) == 1:

    for num in nums:

        cur_avg = num/1

else:
    while j<len(nums):

        sliced_array = nums[i:j]

        cur_avg = (sum(sliced_array))/k

        if cur_avg > avg:

            avg = cur_avg

        i += 1
        j += 1

print(cur_avg)
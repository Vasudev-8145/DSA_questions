"""
sort colors

You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Explanation:
The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Explanation:
The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.
"""

nums = [2,0,2,1,1,0]

count0 = nums.count(0)
count1 = nums.count(1)
count2 = nums.count(2)

index = 0

for i in range(0,count0):

    nums[index] = 0
    index+=1

for i in range(0,count1):

    nums[index] = 1
    index+=1

for i in range(0,count2):

    nums[index] = 2
    index+=1

print(nums)

"""
product of array itself

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

nums = [-1,1,0,-3,3]

product_output = []

for i in range(0,len(nums)):

    mask_num = nums[i]

    nums.remove(mask_num)

    product = 1

    for num in nums:

        product *= num

    product_output.append(product)

    nums.insert(i,mask_num)

print(product_output)
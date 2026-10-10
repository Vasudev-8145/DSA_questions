"""
top k frequent elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
"""

from collections import defaultdict

nums = [1,1,1,2,2,3]
k = 2
count_dict = defaultdict(int)

for n in nums:

    if n not in count_dict:

        count_dict[n] = nums.count(n)


count_list = list(count_dict.values())
count_list.sort(reverse=True)
result_list = []

for each in count_list:

    for key,value in count_dict.items():

        if value == each and key not in result_list:

            result_list.append(key)

    if len(result_list) == k:

        break

print(result_list)
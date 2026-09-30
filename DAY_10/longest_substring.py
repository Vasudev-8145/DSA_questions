"""
Longest substring without repeating character
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

s = "pwwkew"
left = 0
characters = set()
highest_length = 0

for right in range(0,len(s)):

    while s[right] in characters:

        characters.remove(s[left])
        left+=1

    characters.add(s[right])

    current_length = right-left+1

    if current_length > highest_length:

        highest_length = current_length

print(highest_length)

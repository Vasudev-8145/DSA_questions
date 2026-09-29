"""
valid anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""

s = "rat"
t = "car"

sorted_s = sorted(s)
sorted_t = sorted(t)

for ch in sorted_s:

    if ch not in sorted_t and sorted_s.count(ch) != sorted_t.count(ch):

        print(False)
        break

else:

    print(True)


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

for ch in s:

    if ch not in t and s.count(ch)!=t.count(ch):

        print(False)
        break

else:

    print(True)
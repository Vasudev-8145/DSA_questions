"""
isomorphic strings

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:

Input: s = "f11", t = "b23"
Output: false
Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"
Output: true
"""

s = "paper"
t = "title"

char_dict1 = {}
char_dict2 = {}

for i in range(0,len(s)):

    if s[i] in char_dict1 and char_dict1[s[i]] != t[i]:

        print(False)
        break

    if t[i] in char_dict2 and char_dict2[t[i]] != s[i]:

        print(False)
        break

    char_dict1[s[i]] = t[i]
    char_dict2[t[i]] = s[i]

else:

    print(True)




    
"""
word pattern

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 
"""

pattern = "aaaa"
s = "dog cat cat dog"

s_list = s.split(" ")

word_dict1 = {}
word_dict2 = {}

for i in range(0,len(pattern)):

    if pattern[i] in word_dict1 and word_dict1[pattern[i]] != s_list[i]:

        print(False)
        break

    if s_list[i] in word_dict2 and word_dict2[s_list[i]] != pattern[i]:

        print(False)
        break

    word_dict1[pattern[i]] = s_list[i]
    word_dict2[s_list[i]] = pattern[i]

else:

    print(True)
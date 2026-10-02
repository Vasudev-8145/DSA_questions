"""
Ransome note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

magazine = "b"
ransomNote = "a"

for ch in magazine:

    if ch in ransomNote and magazine.count(ch) == ransomNote.count(ch):

        print(True)
        break

else:

    print(False)
"""
valid palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

s = "A man, a plan, a canal: Panama"
new_s = ""

for ch in s:

    if ch.isalnum():

        new_s += ch.lower()

if len(new_s) == 0:

    print(True)

else:

    i = 0
    j = len(new_s)-1

    while i<j:

        if new_s[i] == new_s[j]:
            i += 1
            j -= 1

            result = True

        else:

            result = False
            break

    print(result)

        







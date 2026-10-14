"""
string compressions

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
After modifying the input array in-place, the first 6 characters of chars should be ["a","2","b","2","c","3"].

Example 2:

Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed since it is a single character.
After modifying the input array in-place, the first character of chars should be ["a"].

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
After modifying the input array in-place, the first 4 characters of chars should be ["a","b","1","2"].

"""

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

chars_string = ""
chars_list = []

for ch in chars:

    if ch not in chars_string:

        chars_string += ch

        if chars.count(ch)>1:

            chars_string+=str(chars.count(ch))

for each in chars_string:

    chars_list.append(each)

print(len(chars_list))
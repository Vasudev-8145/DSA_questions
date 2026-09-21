"""
You are given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""

arr = [2,7,11,15]
target = 22

for num in arr:

    difference = target-num

    if difference in arr and difference!=num:

        print([arr.index(num),arr.index(difference)])
        break

else:

    print("No such numbers to meet the condition")


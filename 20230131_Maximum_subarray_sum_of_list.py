# This problem was asked by Facebook.
# 
# Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.
# For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.
# Given [-4, 5, 1, 0], return 6 asy we choose the numbers 5 and 1.

EXAMPLE = [8, -1, 3, 4]  # result: 15
# EXAMPLE = [-4, 5, 1, 0]  # result: 6
# EXAMPLE = [-4, -5, -1, -10]  # result: 0 (no subarray greater than 0, so no subarray selected)
# EXAMPLE = [8, -1, 3, 4, 6, -3, 5, 5, 0, -10, 9, 12, 1]  # result: 49

result = 0
winner_subarray = []

for cycle, _ in enumerate(EXAMPLE):  # no. of rotations
    for idx, _ in enumerate(EXAMPLE):  # no. of subarrays between elements [0..idx+1]
        temp = sum(EXAMPLE[0:idx+1])
        if temp > result: 
            result = temp
            winner_subarray = EXAMPLE[0:idx+1]
    EXAMPLE.insert(0, EXAMPLE.pop())  # we shift/rotate the loop by removing the last element and placing it on the front of the list
    print(EXAMPLE)
        
print("\nMaximum subarray sum of example list is: %s" % result)
print("Winner subarray is: %s" % winner_subarray)
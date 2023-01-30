# This problem was asked by Google.
# 
# Given an array of elements, return the length of the longest subarray where all its elements are distinct.
# For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].


list = [5, 1, 3, 5, 2, 3, 4, 1]
list_collection = []

for pos, digit in enumerate(list):
    found = False
    for endpos, enddigit in enumerate(list[pos+1:]):
        if found: continue
        if enddigit == digit:
            found  = True
            list_collection.append(list[pos:endpos+pos+1])
            
    if not found:
        list_collection.append(list[pos:])

# print(list_collection)
print(max(list_collection))

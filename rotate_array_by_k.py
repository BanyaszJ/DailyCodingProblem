# This problem was asked by Amazon.
# Given an array and a number k that's smaller than the length of the array, 
# rotate the array to the right k elements in-place.

l = [1,"a",2,"b",3,"c"]
# l = [1,2,3,4,5,6,7,8,9,10]
# l = [1,None,3,4,5,6,7,8,None,10]

k = 3
for i in range(k):       
   l.insert(0, l.pop())

print(l)
# This problem was asked by Palantir.
# 
# Write a program that checks whether an integer is a palindrome. 
# For example, 121 is a palindrome, as well as 888. 
# 678 is not a palindrome. 
# Do not convert the integer into a string.

#input
NUM = int(input("gimme a number:"))

#calculate
digits_list = []
while NUM > 0:
    curr = NUM % 10
    digits_list.append(curr)
    NUM = NUM // 10

# decide result
result = "is NOT"
if digits_list == digits_list[::-1]:
    result = "is"    

print("Number %s palindrome!" % result)
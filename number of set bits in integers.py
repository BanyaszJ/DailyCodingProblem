# This problem was asked by Pivotal.

# Write an algorithm that finds the total number of set bits in all integers between 1 and N.

# 0 0
# 1 01
# 2 10
# 3 11

N = 159
result = 0

for i in range(1, N+1):
    result += bin(i).count("1")
    
print("Result: %s" % result)
# forgive me for what i have done, but str.count is totall a legit builtin...
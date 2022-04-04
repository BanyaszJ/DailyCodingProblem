'''Given an array of numbers, find Greatest common denominator of the array elements.'''
input_list = [42, 56, 14]
print("List of nums: %s " % input_list)

def find_gcd(l):
    curr = max(l)
    while curr > 0:
        checker_list = [0 if item%curr==0 else 1 for item in l]
        if sum(checker_list) == 0:
            return curr
        else:
            curr -= 1
            
print("GCD is: %s" % find_gcd(input_list))
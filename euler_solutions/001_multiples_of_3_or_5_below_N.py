import sys

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    n -= 1
    
    threes = n//3
    fives = n//5
    fifteens = n//15
    # eddig ok
    
    
    threes  = 3*threes*(1+threes)>>1
    fives   = 5*fives*(1+fives)>>1
    fifteens= 15*fifteens*(1+fifteens)>>1
    
    print(int(threes+fives-fifteens))

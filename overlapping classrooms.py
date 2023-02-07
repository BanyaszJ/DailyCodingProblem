'''Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.'''

table = [(30,75),
         (0,50),
         (60,150),
         
         # (80,150),
         # (0,59),
         # (0,29),
         # (150,29),
         # (149,29),
         ]
         
min = max = -1
for i in table:
    if i[0] < min or min == -1:
        min = i[0]
    if i[1] > max:
        max = i[1]

rooms_needed = 0
for i in range(min, max):
    print("- Current number between min and max: %s " % i)    
    ctr = 0
    for time_intval in range(len(table)):
        print("-- Current time interval from tables: #%s (%s)" % (time_intval, table[time_intval]))
        if table[time_intval][0] <= i <=  table[time_intval][1]:
            ctr += 1
            print("--- Table #%s contains number %s" % (time_intval, i))
    if ctr > rooms_needed: rooms_needed = ctr
    
print("Total rooms needed: %s" % rooms_needed)

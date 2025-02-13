# python add_numbers.py 10 20  (add_numbers.py -> name of program)
# 10 20 arguments  

import sys

# total arguments
n = len(sys.argv)   #arg[0] name of the program (add_numbers.py)
"""

print("Total arguments passed:", n)

print(sys.argv[0]) 
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

"""
sum = 0 
#sum = int(sys.argv[1]) + int(sys.argv[2]) + int(sys.argv[3])  # convert to int

for i in range(1, n):
    #print(sys.argv[i], end = " ")
    sum = sum + int(sys.argv[i])
print(sum)


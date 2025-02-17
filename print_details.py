# wap to print your name ,weight and age using command line 
# python print_details.py Bob 87.6 24 

# I am Bob and I weigh 87.6kgs and also 24 years old

import sys

name = sys.argv[1]
weight = sys.argv[2]
age = sys.argv[3]

print(f"I am {name} and I weigh {weight} kgs and also {age} years old")
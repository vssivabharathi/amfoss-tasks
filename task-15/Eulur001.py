#!/bin/python3
# appy this code in the hackerrank website to see the exact result

import sys

def sum_of_multiples(n):
    total_sum = 0
  
    for number in range(n):
    
        if number % 3 == 0 or number % 5 == 0:
        
            total_sum += number

    return total_sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = sum_of_multiples(n)
    print(result)

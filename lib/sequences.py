#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return

    fib_array = [0, 1]
    for i in range(2, length):
        
        next_number = fib_array[-1] + fib_array[-2]
        
        fib_array.append(next_number)
        
    print(fib_array)

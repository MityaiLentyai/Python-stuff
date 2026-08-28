#!/usr/bin/env python3

def ft_harvest_total():
    sum = 0
    i = 1
    while i <= 3:
        print(f"Day {i} harvest: ", end="")
        sum += int(input())
        i += 1
    print(f"Total harvest: {sum}")

#!/usr/bin/env python3

def ft_plot_area():
    sum = 0
    for i in range(1, 4):
        print(f"Day {i} harvest: ", end="")
        sum += int(input())
    print(f"Total harvest: {sum}")


ft_plot_area()

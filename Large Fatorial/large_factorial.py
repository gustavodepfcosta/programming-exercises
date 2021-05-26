
"""
Given an integer, find its fatorial value. In an interval from 1 to 100.

N! = N*(N-1)(N-2)(N-3)(N-4)(N-5)(...)(N-1)

"""

integer = 80

def large_factorial(integer):
    real_factorial = 0
    fatorial = integer

    if integer == 1 or integer == 0:
        return str(1)

    for multiplier in range(integer - 1, 0, -1):
        print(fatorial, multiplier)
        fatorial *= multiplier

    return str(fatorial)

large_factorial(integer)
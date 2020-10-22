#!/usr/bin/python3

def to_binary(num):
    ans = ''
    while num > 0:
        ans = str(num % 2) + ans
        num = num // 2
    return ans

def to_trinary(num):
    ans = ''
    while num > 0:
        ans = str(num % 3) + ans
        num = num // 3
    return ans

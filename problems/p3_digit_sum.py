#!/usr/bin/env python3
"""Sum an integer's digits recursively."""
import sys

def digit_sum(number):
    number = abs(number)
    if number < 10:
        return number
    return number % 10 + digit_sum(number // 10)

def main():
    data = sys.stdin.read().strip()
    if data:
        print(digit_sum(int(data)))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Find a target in sorted input using binary search."""
import sys

def binary_search(values, target):
    low, high = 0, len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    if not tokens:
        return
    n = tokens[0]
    values = tokens[1:1 + n]
    target = tokens[1 + n]
    print(binary_search(values, target))

if __name__ == "__main__":
    main()

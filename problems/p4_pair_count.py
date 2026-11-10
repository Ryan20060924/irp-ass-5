#!/usr/bin/env python3
"""Count index pairs whose values sum to the target."""
import sys

def count_pairs(values, target):
    seen = {}
    total = 0
    for value in values:
        total += seen.get(target - value, 0)
        seen[value] = seen.get(value, 0) + 1
    return total

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    if not tokens:
        return
    n, target = tokens[0], tokens[1]
    values = tokens[2:2 + n]
    print(count_pairs(values, target))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Print input words in reverse order."""
import sys

def main():
    words = sys.stdin.read().split()
    print(" ".join(reversed(words)))

if __name__ == "__main__":
    main()

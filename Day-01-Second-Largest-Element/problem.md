# Day 1 - Second Largest Element in an Array

## Problem
Given an array of positive integers `arr[]` of size `n`, find the second largest distinct element in the array.
If it does not exist, return `-1`.

## Approaches
1) Naive (Sorting) – O(n log n), O(1)
2) Two-pass – O(n), O(1)
3) One-pass – O(n), O(1)

## Notes
- Track `largest` and `secondLargest` in one traversal for the optimal approach.

QuickSort Implementation in Python

Description

This project implements the QuickSort algorithm in Python. QuickSort is an efficient, divide-and-conquer sorting algorithm that works by selecting a pivot element, partitioning the array around the pivot, and recursively sorting the left and right subarrays.

Features

Uses the Lomuto partitioning scheme for efficient sorting.

Swaps elements in place to minimize extra memory usage.

Handles various test cases, including empty lists and single-element lists.

Algorithm Explanation

Select a pivot element (the first element in this implementation).

Partition the array so that all elements less than or equal to the pivot are on its left, and all greater elements are on its right.

Recursively apply QuickSort to the left and right partitions.

The base case is when the partition size is 1 or 0.

Code Structure

swap(a, b, arr): Swaps two elements in the array.

partition(arr, start_pointer, end): Partitions the array around the pivot.

quick(arr, start_pointer, end): Recursively sorts the array using QuickSort.

The __main__ block tests the implementation with various cases.

Usage

Running the Script

To run the sorting algorithm, execute:

python quicksort.py

Example Input and Output

Input:

[11, 9, 29, 7, 2, 15, 28]
[3, 7, 9, 11]
[25, 22, 21, 10]
[29, 15, 28]
[]
[6]

Output:

Sorted array: [2, 7, 9, 11, 15, 28, 29]
Sorted array: [3, 7, 9, 11]
Sorted array: [10, 21, 22, 25]
Sorted array: [15, 28, 29]
Sorted array: []
Sorted array: [6]

Complexity Analysis

Best and Average Case (O(n log n)): When the pivot divides the array evenly.

Worst Case (O(n²)): When the pivot is the smallest or largest element, leading to unbalanced partitions.





# heap
Implementation of a heap data structure, along with an implementation of heapsort.

Heap is a usually binary tree type data structure, which has the special property that each parent is larger than both its children. Although, you can always have heaps with more than two children. This implementation however, sticks to a regular binary structure.

## MaxHeap class
Intitalize with `MaxHeap(A)`, where `A` is the list which needs to be represented as a heap. This runs in O(n log n) time.

**NOTE:** If list `A` consists of natively comparable datatypes like int/float/char et cetera, you dont need a second argument. But if your list consists of more complex elements like tuples, lists, or other class objects, a second argument needs to be added, which is defined below:

> `function(a, b) -> returns true if a is greater than b` 

For example, if I want to create a heap from a list of tuples like so, `A = [('a',21),('b',1), ('c',3)]`. And I want to create a heap based on the number in each tuple. I will initialise a MaxHeap object like so: 

> `my_heap = MaxHeap(A, lambda (a,b): a[1] > b[1])`

This lambda function compares the second element of each tuple, and returns True if the first is greater than the second

### Class variables
1. `self.heap`: Store the heap as a list
2. `self.hep_size`: Store the size of the heap (this does not have to be equal to `len(self.heap)`)

### Class methods
1. `get_left(i)` O(1): Return the left child of the i<sup>th</sup> position in the array `A`.
2. `get_right(i)` O(1): Return the right child of the i<sup>th</sup> position in the array `A`.
3. `get_parent(i)` O(1): Return the parent of the i<sup>th</sup> position in the array `A`.
4. `get_heap_size()` O(1): Return the size of the heap.
4. `remove(i)` O(n log n): Remove and return the i<sup>th</sup> element of the heap.
4. `add(to_add)` O(n log n): Add the element `to_add` at the appropriate position in the heap.

## Function heapsort
A comparison sort that runs in O(n log n) time. It creates a MaxHeap data structure from the list. It extracts the root and recreates the heap repeatedly. 

Accepts a list, and returns a sorted list.

#### Simple application function
The function `isAnagram(s1,s2)` in [this file](anagram.py), accepts two strings, uses the function heapsort, and the class MaxHeap to tell if the strings `s1` and `s2` are anagrams. This also runs in O(n log n).

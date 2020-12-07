# heap
Implementation of a heap data structure, along with an implementation of heapsort.

## Heap class
Intitalize with `Heap(A)`, where `A` is the list which needs to be represented as a heap. This runs in O(n log n) time.

**NOTE:** List `A` must consist of natively comparable datatypes like int/float/char et cetera. This is because the building of heap needs value comparison.

### Class methods
1. `get_left(i)` O(1): Return the left child of the i<sup>th</sup> position in the array `A`.
2. `get_right(i)` O(1): Return the right child of the i<sup>th</sup> position in the array `A`.
3. `get_parent(i)` O(1): Return the parent of the i<sup>th</sup> position in the array `A`.
4. `get_heap_size()` O(1): Return the size of the heap.

## Functionality to add:
* Addition and deletion from heap
* Function as an argument for comparison of elements. 

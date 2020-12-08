from heap import MaxHeap

def heapsort(A, greater):
    wh = MaxHeap(A, greater)
    for i in range(len(A)-1, 0, -1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        wh.heap_size -= 1
        wh.heapify(0)
    return wh.heap

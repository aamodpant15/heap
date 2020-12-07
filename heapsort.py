from heap import MaxHeap

def heapsort(word):
    A = list(word)
    # print("    Making Heap")
    wh = MaxHeap(A) #word heap
    # print("From heapsort: "+str(wh.heap))
    # print("    Made Heap: " + str(wh.heap))
    # print()
    # print("    Sorting Heap")
    for i in range(len(A)-1, 0, -1):
        # print(i)
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        wh.heap_size -= 1
        wh.heapify(0)
    # print("\n    Sorted Heap" + str(wh.heap))
    return ''.join(wh.heap)

def isAnagram (s1, s2):
    # classes = dict()

    if len(s1) != len(s2):
        print("False")
    
    # print("Sorting word 1:")
    ss1 = heapsort(s1)

    # print('\n===============\n')

    # print("Sorting word 2:")
    ss2 = heapsort(s2)
    
    if ss1 == ss2:
        print("True")
    else:
        print("False")

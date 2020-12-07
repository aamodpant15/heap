class MaxHeap:
    def __init__(self, A):
        self.heap = A
        self.heap_size = len(A)
        self.build_heap()

    def get_left(self, i):
        return (2*i)+1
    def get_right(self, i):
        return (2*i)+2
    def get_parent(self, i):
        return int(i/2)
    def get_heap_size(self):
        return self.heap_size
    
    def heapify(self, i):
        # print("        From heapify : "+ str(self.heap))
        A = self.heap
        l = self.get_left(i)
        r = self.get_right(i)
    
        # print("\n        i=" + str(i))
        # print("        l = " + str(l))
        # print("        r = " + str(r))
        # print("        size = " + str(self.get_heap_size()))
        # print('\n')
        
        if l < self.get_heap_size() and A[l] > A[i]:
            # print("        Comparing "+ A[l] + ", "+  A[i])
            largest = l
        else:
            largest = i

        if r < self.get_heap_size() and A[r] > A[largest]:
            # print("        Comparing "+ A[r] + ", "+  A[largest])
            largest = r
        if largest != i:
            # print("        Swapping "+ A[i] + ", "+  A[largest])
            temp = A[i]
            A[i] = A[largest]
            A[largest] = temp
            self.heapify(largest)
    
    def build_heap(self):
        # A = self.heap
        for i in range(int(self.heap_size/2),-1,-1):
            # print("i=" + str(i))
            self.heapify(i)

####################################################################################

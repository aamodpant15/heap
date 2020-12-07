"""
REQUIRES THE FUNCTION HEAPSORT
"""

from heap import MaxHeap

def isAnagram (s1, s2):

    if len(s1) != len(s2):
        print("False")
        return False

    # print("Sorting word 1:")
    ss1 = heapsort(s1) # Sorted s1

    # print("Sorting word 2:")
    ss2 = heapsort(s2) # Sorted s2

    if ss1 == ss2:
        print("True")
        return True
    else:
        print("False")
        return False

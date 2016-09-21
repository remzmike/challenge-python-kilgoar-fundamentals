# python 2
# m.k.

# 11. Write a function in the language of your choice that implements
#    quicksort on an array of integers.

def partition(A, lo, hi):
    i = lo - 1
    j = lo
    pivot = A[hi]
    while j <= hi - 1:
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
        j = j + 1
    A[i + 1], A[hi] = A[hi], A[i + 1]
    return i + 1

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
quicksort(array, 0, len(array)-1)
assert array == [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]
array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
quicksort(array, 2, 4)
assert array == [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
quicksort(array, 1, len(array)-2)
assert array == [9, 2, 3, 5, 7, 10, 11, 12, 14, 6]

# 12. Write a function in the language of your choice that performs
#    binary search on a sorted array of integers.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binary_search(A, x, lo, hi):
    while lo < hi:
        i = (lo+hi)//2
        if A[i] < x:
            lo = i + 1
        elif A[i] > x:
            hi = i
        else:
            return i
    return -1

lo = 0
hi = len(array)-1
assert binary_search(array, 13, lo, hi)==-1
assert binary_search(array, 1, lo, hi)==0
assert binary_search(array, 1, lo+1, hi)==-1
assert binary_search(array, 8, lo, hi)==7
assert binary_search(array, 8, lo, 8)==7
assert binary_search(array, 8, lo, 7)==-1
assert binary_search(array, -2, lo, hi)==-1

# 14. Write a program in the language of your choice that takes a filename
#     and a number N as arguments and retrieves and outputs the Nth line
#     from the file.

def get_line(fpath, n):
    with open(fpath, 'rb') as f:
        line_count = 0
        for line in f:
            line_count = line_count + 1
            if line_count == n:
                return line.rstrip('\n\r')
        
#print(repr(get_line('c:/tmp.py',18)))
if __name__=='__main__':
    import sys
    print(get_line(sys.argv[1], int(sys.argv[2])))

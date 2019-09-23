'''
Ismael Villalobos
9-22-19
Lab Assignment 2
Professor Fuentes
TA-Dita Nath
Purpose: Implementing sorting algorithms like bubble sort and 
quick sort to understand how they function, implement quick sort
using a stack and implement modified with no stack or recursion. 
Understand the differences in their run times.
    
'''

import time
import random
def select_bubble(L,k):
    for i, num in enumerate(L):
        try:
            if L [i+1] < num:
                L[i] = L[i+1]
                L[i+1] = num
                select_bubble(L, k)
        except IndexError:
            pass
    return L[k]

def partition(L,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = L[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   L[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            L[i],L[j] = L[j],L[i] 
  
    L[i+1],L[high] = L[high],L[i+1] 
    return ( i+1 )

def quickSort(L,low,high):
    if low < high: 
        p = partition(L,low,high) 
        quickSort(L, low, p-1) 
        quickSort(L, p+1, high) 
    return L
        
def select_quick(L,k):
    if (k < 0) or (k >= len(L)) or (len(L) <= 0):
        return False
    q = quickSort(L,0,len(L)-1)
    return q[k]


def quickSort_modified(L,low,high):
    while low < high: 
        p = partition(L,low,high) 
        quickSort_modified(L, low, p-1) 
        low = p+1 
    return L
def select_modified_quick(L,k):
    if (k < 0) or (k >= len(L)) or (len(L) <= 0):
        return -1
    quickSort_modified(L, 0,len(L)-1)
    return L[k]
    
def quickSort_stack(L,low,high,k):
    stack = [[L,low,high]]
    while len(stack) >0:
        block = stack.pop(-1)
        if block[1]>block[2]:
            p = partition(block[0],block[1],block[2])
            stack.append(L,low, p-1)
            stack.append(L,p+1,high)
    return L[k]

def select_quick_while(L, low, high, k):
    pivot = partition(L, low, high)

    while pivot != k:
        if k > pivot:
            pivot = partition(L, pivot + 1, high)
        elif k < pivot:
            pivot = partition(L, low, pivot - 1)
    return L[pivot]

list_length = 100
L1 = [random.randint(0,5000) for i in range(list_length)]

#print(L1.sort())

print('=====================PART1=========================')

k = 0
while (True):
    try:
        k = int(input('Enter a value for k:'))
        break
    except: 
        print('Please enter a positive integer number.\n')
        
if (k >= len(L1)) or k < 0:
        print("\nError: Value for k out of bounds. List size:", len(L1), "\n")
else:
    #bubble 
    start = time.time()
    pos = select_bubble(L1,k)
    stop = time.time()
    
    runTime= stop-start
    print('Using BubbleSort')
    print('Kth smallest element at position',k,' smallest element is ',pos)
    print("It took","{:.9f}".format(runTime), "seconds to sort and find k.")

    #quick 
    start = time.time()
    pos = select_quick(L1,k)
    stop = time.time()
    
    runTime= stop-start
    print('Using QuickSort')
    print('Kth smallest element at position',k,' smallest element is ',pos)
    print("It took","{:.9f}".format(runTime), "seconds to sort and find k.")


    #modded quick 
    start = time.time()
    pos = select_modified_quick(L1,k)
    stop = time.time()
    
    runTime= stop-start
    print('Using Modified QuickSort Sort')
    print('Kth smallest element at position',k,' smallest element is ',pos)
    print("It took","{:.9f}".format(runTime), "seconds to sort and find k.")
    
    print('=====================PART2=========================')

    # quicksort with stack implem.
    start = time.time()
    pos = quickSort_stack(L1,0,len(L1)-1,k)
    stop = time.time()
    
    runTime= stop-start
    print('Using QuickSort using Stacks')
    print('Kth smallest element at position',k,' smallest element is ',pos)
    print("It took","{:.9f}".format(runTime), "seconds to sort and find k.")

    # quicksort with a while loop
    start = time.time()
    pos = select_quick_while(L1,0,len(L1)-1,k)
    stop = time.time()
    
    runTime= stop-start
    print('Using QuickSort While Loop')
    print('Kth smallest element at position',k,' smallest element is ',pos)
    print("It took","{:.9f}".format(runTime), "seconds to sort and find k.")


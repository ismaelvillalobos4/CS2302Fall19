'''
    Course: CS2302 Data Structures Fall 2019
    Author: Ismael Villalobos
    Assignment: Lab 3 Linked Lists
    Instructor: Dr. Olac Fuentes
    TA: Anindita Nath 
    Last Modified: October 5th 2019
    Purpose: 
'''

import math
import random


class Node(object):
    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# SortedList functions
class SortedList(object):
    # constructor
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def Print(self):
        # prints items in order using a loop
        t = self.head
        while t is not None:
            print(t.data, end=' ')
            t = t.next
        print()

    def Append(self, x):
        node = Node(x)
        current = self.head
        previous = None

        while current is not None and current.data < x:
            previous = current
            current = current.next

        if previous == None:
            self.head = node
        else:
            previous.next = node

            node.next = current

    def Insert(self, i):
        self.Append(i)

    def Delete(self, i):
        t = self.head

        if t is None:
            return None
        elif t.data == i:
            if t.next is None:
                self.head = None
            else:
                self.head = t.next
        else:
            prev = t
            while t is not None:
                if t.data == i:
                    prev.next = t.next
                prev = t
                t = t.next

    def Merge(self, M):
        x = M.head
        while x is not None:
            self.Insert(x.data)
            x = x.next

    def IndexOf(self, i):
        t = self.head
        index = 0
        while t is not None:
            if t.data == i:
                return index
            index += 1
            t = t.next
        return -1

    def Clear(self):
        self.head = None

    def Min(self):
        if self.head is None:
            return math.inf
        return self.head.data

    def Max(self):
        t = self.head
        if t is None:
            return -math.inf
        max = -math.inf
        while t is not None:
            if t.data > max:
                max = t.data
            t = t.next
        return max

    def HasDuplicates(self):
        t = self.head
        if t is None or t.next is None:
            return False
        while t is not None:
            if t.next != None:
                if t.data == t.next.data:
                    return True
            t = t.next
        return False

    def Select(self, k):
        if self.head is None:
            return math.inf
        index = 0
        t = self.head
        while t is not None:
            if index == k:
                return t.data
            index += 1
            t = t.next


L = SortedList()  # create empty list to use for main output
M = SortedList()  # list for merging

# fill list with random values between 0-50
for i in range(0, 10):
    L.Append(i)

for i in range(0, 10):
    M.Append(random.randint(0, 50))
print('Printing Items In Sorted List')
L.Print()
insertion= int(input('Enter number to insert: '))
print('Inserting',insertion)
print('List after inserting',insertion)
L.Insert(insertion)
L.Print()
deletion= int(input('Enter number to delete: '))
print('Deleting',deletion)
print('List after deleting',deletion)
L.Delete(deletion)
L.Print()

print('====================================')
print('This is L')
L.Print()
print('This is M')
M.Print()

print('This is L and M Merged')
L.Merge(M)
L.Print()
key = int(input("Enter a number to find in the list: "))
print(key, "is found at the following index:", L.IndexOf(key))
print('Clearing List')
L.Clear()
print('List Cleared')
L.Print()
print('Creating New List')
for i in range(0, 10):
    L.Append(random.randint(0, 50))
print('New List Is')
L.Print()

m = L.Min()
print('Minimum Value in List',m)
mx = L.Max()
print('Maximum Value in List',mx)

print('Checking for Duplicates')
L.Print()
dup=L.HasDuplicates()
if dup == True:
    print('List Contains Duplicates')
else:
    print('List Does Not Contain Duplicates')
K = int(input("Enter a number for k: "))
print("Value at position k:", L.Select(K))



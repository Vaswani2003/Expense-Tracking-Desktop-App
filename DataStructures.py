import sys

import sys

class PriorityQueue:
    def __init__(self, maxsize):
        self.max_size = maxsize
        self.size = 0
        self.heap = [None] * (self.max_size + 1)
        self.front = 1

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.max_size

    def left_child(self, index):
        return 2 * index
    
    def right_child(self, index):
        return 2 * index + 1
    
    def parent(self, index):
        return index // 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class MinHeap(PriorityQueue):
    def __init__(self, maxsize):
        super().__init__(maxsize)

    def min_heapify(self, index):
        left = self.left_child(index)
        right = self.right_child(index)
        smallest = index

        if left <= self.size and int(self.heap[left]['amount']) < int(self.heap[smallest]['amount']):
            smallest = left
        if right <= self.size and int(self.heap[right]['amount']) < int(self.heap[smallest]['amount']):
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.min_heapify(smallest)
        
    def insert(self, element):
        if self.is_full():
            print("Heap is full!")
            return
        
        self.size += 1
        self.heap[self.size] = element
        current = self.size

        while current > 1 and int(self.heap[current]['amount']) < int(self.heap[self.parent(current)]['amount']):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        if self.is_empty():
            print("Heap is empty!")
            return None

        root = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.min_heapify(self.front)
        return root


class MaxHeap(PriorityQueue):
    def __init__(self, maxsize):
        super().__init__(maxsize)

    def max_heapify(self, index):
        left = self.left_child(index)
        right = self.right_child(index)
        largest = index

        if left <= self.size and int(self.heap[left]['amount']) > int(self.heap[largest]['amount']):
            largest = left
        if right <= self.size and int(self.heap[right]['amount']) > int(self.heap[largest]['amount']):
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.max_heapify(largest)
        
    def insert(self, element):
        if self.is_full():
            print("Heap is full!")
            return
        
        self.size += 1
        self.heap[self.size] = element
        current = self.size

        while current > 1 and int(self.heap[current]['amount']) > int(self.heap[self.parent(current)]['amount']):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        if self.is_empty():
            print("Heap is empty!")
            return None

        root = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.max_heapify(self.front)
        return root



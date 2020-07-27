import numpy as np
#by importing numpy we can save inputs as a matrix and thats easier
#making a min heap class
class Heap:
    def __init__(self):
        self.a = []
    def min_heapify(self,i,n):
        left = 2*i+1
        right = 2*i+2
        if left < n and self.a[i] > self.a[left]:
            smallest = left
        else:
            smallest = i
        if right < n and self.a[smallest] > self.a[right]:
            smallest = right
        if i != smallest:
            self.a[i],self.a[smallest] = self.a[smallest],self.a[i]
            self.min_heapify(smallest,n)
    def build_min_heap(self):
        for i in range(len(self.a)//2,-1,-1):
            self.min_heapify(i,len(self.a))
    def heapSort(self):
        #self.build_min_heap()
        for i in range(len(self.a)-1,0,-1):
            self.a[0],self.a[i] = self.a[i],self.a[0]
            self.min_heapify(0,i)
    def heap_decrease_key(self,i,key):
        if self.a[i] < key:
            return
        self.a[i] = key
        while i > 0 and self.a[i] < self.a[(i-1)//2]:
            self.a[i],self.a[(i-1)//2] = self.a[(i-1)//2],self.a[i]
            i = (i-1)//2
    def heap_insert(self,key):
        self.a.append(10000000)
        self.heap_decrease_key(len(self.a)-1,key)
    def print_heap(self):
        print(self.a)
    def printMin(self):
        print('Minimum: ',self.a[0])
n = int(input("Please enter n: "))
k = int(input("Please enter k: "))
finalList = []
for i in range(3):
    #getting arrays in once *Please enter numbers with a space between
    initialList = list(map(int,input("Please enter row "+str(i+1)+": ").split()))
    finalList.append(initialList)
#making matrix
myArray = np.array(finalList)
#making a heap instance
myHeap = Heap()
initialList = []
sum = 0
#working on it for all values of t less than k
for t in range(k):
    for i in range(3):
        for j in myArray[i]:
            sum += (j+t)%k
        initialList.append(sum)
        sum = 0
    myHeap.heap_insert(max(initialList))
    initialList = []
myHeap.print_heap()
myHeap.printMin()

    

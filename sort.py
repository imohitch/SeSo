from queue import Queue
from heap import MaxHeap

class RadixSort:
  def __init__(self, arr, maxDigitSize):
    self.arr = arr
    self.maxDigitSize = maxDigitSize

  def _radixSort(self, arr, maxDigitSize):
    binArray = [None]*10
    for k in range(10):
      binArray[k] = Queue(0)
  
    column = 1

    for _ in range(maxDigitSize):
      for key in arr:
        digit = (key // column) % 10
        binArray[digit].put(key)

      i=0
      for bin in binArray:
        while not bin.empty():
          arr[i] = bin.get()
          i+=1
      column *= 10

  def sort(self):
    self._radixSort(self.arr, self.maxDigitSize)

class QuickSort:
  def __init__(self, arr):
    self.arr = arr

  def _partitionArray(self, arr, first, last):
    pivot = arr[first]
    left = first+1
    right = last
    
    while left <= right:
      while left <= right and arr[left] <= pivot:
        left+=1
      while left <= right and arr[right] >= pivot:
        right-=1
      if left<right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

    if first != right:
      arr[first] = arr[right]
      arr[right] = pivot

    return right

  def _quickSort(self, arr, first, last):
    if first < last:
      pos = self._partitionArray(arr, first, last)
      self._quickSort(arr, first, pos-1)
      self._quickSort(arr, pos+1, last)

  def sort(self):
    self._quickSort(self.arr, 0, len(self.arr)-1)

class MergeSort:
  def __init__(self, arr):
    self.arr = arr
    self.arrT = [0]*len(arr)

  def _arrayMerge(self, arr, left, right, end, arrT):
    a = left
    b = right
    m = 0
    while a < right and b < end:
      if arr[a] < arr[b]:
        arrT[m] = arr[a]
        a+=1
      else:
        arrT[m] = arr[b]
        b+=1
      m+=1

    while a < right:
      arrT[m] = arr[a]
      a+=1
      m+=1

    while b < end:
      arrT[m] = arr[b]
      b+=1
      m+=1

    for i in range (m):
      arr[i+left] = arrT[i]

  def _mergeSort(self, arr, first, last, arrT):
    if first!=last:
      mid = (first+last) // 2
      self._mergeSort( arr, first, mid, arrT)
      self._mergeSort( arr, mid+1, last, arrT)
      self._arrayMerge( arr, first, mid+1, last+1, arrT)

  def sort(self):
    self._mergeSort(self.arr, 0 , len(self.arr)-1, self.arrT)

class Heapsort:
  def __init__(self, arr):
    self.maxheap = MaxHeap(len(arr))
    for key in arr:
      self.maxheap.add(key)

  def sort(self):
    while self.maxheap.count > 0:
      self.maxheap.elements[self.maxheap.count] = self.maxheap.extract()
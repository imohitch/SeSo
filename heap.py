class MaxHeap:
  def __init__(self, maxSize):
    self.elements = [None]*maxSize
    self.count = 0

  def capacity(self):
    return len(self.elements)

  def add(self, key):
    assert self.count < self.capacity(), "Heap is already full"
    self.elements[self.count] = key
    self.count += 1
    self._siftUp(self.count - 1)

  def _siftUp(self, index):
    if index > 0:
      parent = index // 2
      if self.elements[index] > self.elements[parent]:
        tmp = self.elements[index]
        self.elements[index] = self.elements[parent]
        self.elements[parent] = tmp
        self._siftUp(parent)

  def extract(self):
    assert self.count > 0, "Can extract from an empty heap"
    value = self.elements[0]
    self.count -= 1
    self.elements[0] = self.elements[self.count]
    self.elements[self.count] = None
    self._siftDown(0)
    return value
  
  def _siftDown(self, index):
    left = index*2 + 1
    right = index*2 + 2
    largest = index
    
    if left < self.count and self.elements[left] >= self.elements[largest]:
      largest = left
    
    if right < self.count and self.elements[right] >= self.elements[largest]:
      largest = right
    
    if largest != index:
      tmp = self.elements[index]
      self.elements[index] = self.elements[largest]
      self.elements[largest] = tmp
      self._siftDown(largest)
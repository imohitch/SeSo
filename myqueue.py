# Skipping implementation of basic queue and using build-in Queue class in python
from queue import Queue

# Below is fix range priority implementation
# For unbound priority implementation, use MaxHeap with a storageNode class
class PriorityQueueBound:
  def __init__(self, maxSize):
    self.maxSize = maxSize
    self.levelArray = [None]*maxSize
    for i in range(maxSize):
      self.levelArray[i] = Queue()

    self.top = -1
    self.taskCount = 0

  def put(self, priority, task):
    if priority > -1 and priority < self.maxSize:
      q = self.levelArray[priority]
      q.put(task)
      self.taskCount += 1
      if priority > self.top:
        self.top = priority

  def adjustTop(self):
    if self.taskCount == 0:
      self.top = -1
    else:
      for level in range(self.top-1, -1, -1):
        if not self.levelArray[level].empty():
          self.top = level
          break

  def get(self):
    if self.top > -1:
      q = self.levelArray[self.top]
      task = q.get()
      self.taskCount -= 1
      if q.empty():
        self.adjustTop()
      return task
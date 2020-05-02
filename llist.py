class ListNode:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class Llist:
  def __init__(self):
    self.head = None

  def prepend(self, data):
    newNode = ListNode(data)
    newNode.next = self.head
    self.head = newNode

  def append(self, data):
    if self.head is None:
      self.head = ListNode(data)
    else:
      curNode = self.head
      while curNode.next != None:
        curNode = curNode.next
      curNode.next = ListNode(data)

  def insert(self, data):
    if self.head is None:
      self.head = ListNode(data)
    else:
      prevNode = None
      curNode = self.head
      while curNode is not None and curNode.data < data:
        prevNode = curNode
        curNode = curNode.next
      newNode = ListNode(data)
      newNode.next = curNode
      if curNode is self.head:
        self.head = newNode
      else:
        prevNode.next = newNode

  def traverse(self):
    curNode = self.head
    while(curNode != None):
      print(curNode.data)
      curNode = curNode.next

  def remove(self, data):
    curNode = self.head
    prevNode = None
    while curNode.next is not None and curNode.data != data:
      prevNode = curNode
      curNode = curNode.next

    if curNode is not None:
      if curNode is self.head:
        temp = self.head
        self.head = self.head.next
        del(temp)
      else:
        prevNode.next = curNode.next
        del(curNode)

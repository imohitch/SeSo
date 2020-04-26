from queue import Queue, LifoQueue

# Storage class for BST node
class _BSTNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

# BST class
class BST:
  def __init__(self):
    self.root = None
    self.size = 0

  # Add a new node to BST
  def add(self, key):
    self.root = self._insert(self.root, key)
  
  def _insert(self, subtree, key):
    if subtree is None:
      subtree = _BSTNode(key)
      self.size += 1
    elif key < subtree.key:
      subtree.left = self._insert(subtree.left, key)
    elif key > subtree.key:
      subtree.right = self._insert(subtree.right, key)
    return subtree

  # Check if a node is present in BST
  def isPresent(self, key):
    return self._search(self.root, key) is not None
  
  def _search(self, subtree, key):
    if subtree is None:
      return None
    elif key < subtree.key:
      return self._search(subtree.left, key)
    elif key > subtree.key:
      return self._search(subtree.right, key)
    else:
      return subtree

  # Traverse a BST dfs manner
  def preorder_traverse(self):
    self._traverse(self.root, "pre")

  def inorder_traverse(self):
    self._traverse(self.root, "in")

  def postorder_traverse(self):
    self._traverse(self.root, "post")

  def _traverse(self, subtree, order):
    if subtree is not None:
      if order == "pre":
        print(subtree.key)
      
      self._traverse(subtree.left, order)

      if order == "in":
        print(subtree.key)

      self._traverse(subtree.right, order)

      if order == "post":
        print(subtree.key)

  # Traverse a BST in bfs manner
  # To traverse bottomup push into stack instead of print
  def topdown_traverse(self):
    nodesQueue = Queue()
    nodesQueue.put(self.root)
    while not nodesQueue.empty():
      node = nodesQueue.get()
      print(node.key)
      if node.left is not None:
        nodesQueue.put(node.left)
      if node.right is not None:
        nodesQueue.put(node.right)

  def bottomup_traverse(self):
    nodesQueue = Queue()
    nodesStack = LifoQueue()
    nodesQueue.put(self.root)
    
    while not nodesQueue.empty():
      node = nodesQueue.get()
      nodesStack.put(node)
      if node.left is not None:
        nodesQueue.put(node.left)
      if node.right is not None:
        nodesQueue.put(node.right)
    
    while not nodesStack.empty():
      node = nodesStack.get()
      print(node.key)      

  # Get node with minimum value in BST
  def findMinKeyNode(self):
    assert self.root is not None, "Tree is empty"
    return self._findMinKeyNode(self.root)

  def _findMinKeyNode(self, subtree):
    if subtree is None:
      return None
    elif subtree.left is None:
      return subtree
    else:
      return self._findMinKeyNode(subtree.left)

  # Get node with maximum value in BST
  def findMaxKeyNode(self):
    assert self.root is not None, "Tree is empty"
    return self._findMaxKeyNode(self.root)

  def _findMaxKeyNode(self, subtree):
    if subtree is None:
      return None
    elif subtree.right is None:
      return subtree
    else:
      return self._findMaxKeyNode(subtree.right)

  # Delete a node is present in BST
  def delete(self, key):
    self.root = self._delete(self.root, key)

  def _delete(self, subtree, key):
    if subtree is None:
      return subtree
    elif key < subtree.key:
      subtree.left = self._delete(subtree.left, key)
      return subtree
    elif key > subtree.key:
      subtree.right = self._delete(subtree.right, key)
      return subtree
    else:
      if subtree.left is None and subtree.right is None:
        del(subtree)
        self.size -= 1
        return None
      elif subtree.left is None or subtree.right is None:
        self.size -= 1
        if subtree.left is not None:
          left = subtree.left
          del(subtree)
          return left
        else:
          right = subtree.right
          del(subtree)
          return right
      else:
        successor = self._findMinKeyNode(subtree.right)
        subtree.key = successor.key
        subtree.right = self._delete(subtree.right, successor.key)
        return subtree

  
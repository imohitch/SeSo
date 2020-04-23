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

  # Traverse a BST
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
  def _findMaxKeyNode(self, subtree):
    if subtree is None:
      return None
    elif subtree.right is None:
      return subtree
    else:
      return self._findMaxKeyNode(subtree.right)

  def findMaxKeyNode(self):
    assert self.root is not None, "Tree is empty"
    return self._findMaxKeyNode(self.root)

  
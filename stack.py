class StackNode:
  def __init__(self, data=None, link=None):
    self.data = data
    self.next = link

class LLStack:
  def __init__(self):
    self.size = 0
    self.top = None

  def isEmpty(self):
    return self.top is None

  def peek(self):
    if self.size > 0:
      return self.top.data

  def put(self, data):
    self.top = StackNode(data, self.top)
    self.size += 1

  def get(self):
    if self.size > 0:
      top = self.top
      self.top = self.top.next
      self.size -= 1
      return top.data

class ArrayStack:
  def __init__(self, maxSize):
    self.maxSize = maxSize
    self.top = -1
    self.arr = [None]*maxSize

  def isEmpty(self):
    return self.top < 0

  def isFull(self):
    return self.top >= self.maxSize - 1

  def peek(self):
    if not self.isEmpty():
      return self.arr[self.top]

  def put(self, data):
    if not self.isFull():
      self.top += 1
      self.arr[self.top] = data

  def get(self):
    if not self.isEmpty():
      self.top -= 1
      return self.arr[self.top + 1]


class InfixToPostfix:
  def __init__(self, infixexpr):
    self.infixexpr = infixexpr
    self.postfixList = []
    self.infixToPostfix()

  def postfixExp(self):
    return "".join(self.postfixList) 

  def infixToPostfix(self):
    prec = {
      "*" : 3,
      "/" : 3,
      "+" : 2,
      "-" : 2,
      "(" : 1
    }
    opStack = ArrayStack(len(self.infixexpr))

    for token in self.infixexpr:
      if token == ' ':
        continue
      if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
        self.postfixList.append(token)
      elif token == '(':
        opStack.put(token)
      elif token == ')':
        topToken = opStack.get()
        while topToken != '(':
          self.postfixList.append(topToken)
          topToken = opStack.get()
      else:
        while (not opStack.isEmpty()) and \
        (prec[opStack.peek()] >= prec[token]):
          self.postfixList.append(opStack.get())
        opStack.put(token)

    while not opStack.isEmpty():
      self.postfixList.append(opStack.get())

  def performOp(self, x, y, op):
    if op == '/':
      return x/y
    elif op == '*':
      return x*y
    elif op == '-':
      return x-y
    else:
      return x+y

  def evalPostfixExp(self, tokenVals):
    stack = ArrayStack(len(self.postfixList))
    for token in self.postfixList:
      if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        stack.put(tokenVals[token])
      if token in "0123456789":
        stack.put(token)
      if token in '*/-+':
        right = stack.get()
        left = stack.get()
        stack.put(self.performOp(left, right, token))
    return stack.get()

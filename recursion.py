# Optimized Fibonacci using dictionary
class Fibonnaci:
  def __init__(self):
    self.d={}

  def fibonacci(self, num):
    return self._fibonacci(num)

  def _fibonacci(self, num):
    assert num >=1, "Compute atleast 3rd fibonacci number"
    if num == 1 or num == 2:
      return 1
    else:
      if num in self.d:
        return self.d[num]
      else:
        self.d[num] = self._fibonacci(num - 1) + self._fibonacci(num - 2)
        return self.d[num]

# We can't optimize factorial using a dict because any result isn't reused
class Factorial:
  def factorial(self, num):
    assert num >= 0, "-ve factorial not defined"
    if num == 0:
      return 1
    else:
      return num * self.factorial(num -1)

class TowerOfHanoi:
  def move(self, n, src, temp, dst):
    if n>=1:
      self.move(n-1, src, dst, temp)
      print("move ", str(n), " from ", src, " to ", dst)
      self.move(n-1, temp, src, dst)

class Exp:
  def exp(self, x, n):
    assert x>=1, "X should be greater or equal to 1"
    return self._exp(x, n)
  
  def _exp(self, x, n):
    if n == 0:
      return 1
    result = self._exp(x * x, n//2 )
    if n%2 == 0:
      return result
    else:
      return x * result
# Solution 1: 
# We can easy solve this problem with O(n^2)
# n = int(input())
# a = list(map(int,input().split()))
# min_loss = int(1e15 + 1)

# for i in range(n):
#   for j in range(i+1, n):
#     loss = a[i] - a[j]
#     if loss > 0 and loss < min_loss:
#       min_loss = loss

# print(min_loss)

# Solution 2: We see that O(n^2) approach is not optimal solution
# We notice that "a" is a distinct array, so we think of a tree that contain the array
# -> so we build a binary tree with the cost is n*log(n) with n is number of houses
# we find the upperbound of new added element -> then cal the loss and compare to the min_loss

class Node:
   def __init__(self, value):
      self.value = value
      self.left = self.right = None

def insert(root, x):
  if root is None:
      return Node(x)
  if x < root.value:
      root.left = insert(root.left, x)
  elif x > root.value:
      root.right = insert(root.right, x)
  return root

def upperbound(root, x):
  if root is None:
      return root
  if root.value <= x:
      return upperbound(root.right, x)
  elif root.value > x:
      ub_left = upperbound(root.left, x)
      return root if ub_left is None else ub_left

n = input()
prices = list(map(int, input().split()))

min_loss = 10 ** 16
root = None

for sell_price in prices:
  best_buy_node = upperbound(root, sell_price)
  if best_buy_node is not None:
      loss = best_buy_node.value - sell_price
      min_loss = min(loss, min_loss)
  root = insert(root, sell_price)

print(min_loss)
class Node:
  def __init__(self) -> None:
      self.countW = 0
      self.n_common = 0
      self.child = dict()

def addWord(root, s):
  temp = root
  for ch in s:
    if ch not in temp.child:
      temp.child[ch] = Node()
    temp = temp.child[ch]
    temp.n_common += 1

  temp.countW += 1

def findWord(root, s):
  temp = root
  for ch in s:
    if ch not in temp.child:
      return 0
    temp = temp.child[ch]
  return temp.n_common

def main():
  root = Node()
  n = int(input())
  for _ in range(n):
    cmd, word = input().split()
    if cmd == "add": addWord(root, word)
    elif cmd == "find":
      print(findWord(root, word))

main()
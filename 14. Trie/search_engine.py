class Node:
  def __init__(self, countWord = 0, piority = 0):
    self.piority = piority 
    self.child = dict()
    
n, q = map(int, input().split())

def addWord(root, s, p):
  cur = root
  for ch in s:
    if ch not in cur.child:
      cur.child[ch] = Node(0, p)
    cur = cur.child[ch]
    cur.piority = max(cur.piority, p)

def findWord(root, s):
  cur = root
  for ch in s:
    if ch not in cur.child:
      return -1
    cur = cur.child[ch]
  return cur.piority

root = Node()

for i in range(n):
  word, pior = input().split()
  addWord(root, word, int(pior))
for i in range(q):
  word = input()
  print(findWord(root, word))
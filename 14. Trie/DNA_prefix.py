class Node:
  def __init__(self) -> None:
      self.n_common = 0
      self.child = dict()

def addWord(root, s, res):
  temp = root
  for i in range(len(s)):
    ch = s[i]
    level = i + 1
    if ch not in temp.child:
      temp.child[ch] = Node()
    temp = temp.child[ch]
    temp.n_common += 1
    res = max(res, temp.n_common * level)
  return res


T = int(input())

for tc in range(T):
  n = int(input())
  root = Node()
  res = 0
  for _ in range(n):
    word = input()
    res = addWord(root, word, res)
  print(f"Case {tc+1}: {res}")
  


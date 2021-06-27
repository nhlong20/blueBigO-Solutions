class Node:
  def __init__(self) -> None:
      self.countW = 0
      self.child = dict()

def addWord(root, s):
  temp = root
  has_other_as_prefix = False
  is_prefix_of_other = True
  
  for ch in s:
    if ch not in temp.child:
      temp.child[ch] = Node()
      is_prefix_of_other = False
    temp = temp.child[ch]
    if temp.countW == 1:
      has_other_as_prefix = True

  temp.countW = 1
  return is_prefix_of_other or has_other_as_prefix


T = int(input())

for tc in range(T):
  n = int(input())
  root = Node()

  is_not_consistent = False
  for _ in range(n):
    if not is_not_consistent:
      is_not_consistent = addWord(root, input())
    else: input()

  res = 'NO' if is_not_consistent else 'YES'
  print(f"Case {tc+1}: {res}")

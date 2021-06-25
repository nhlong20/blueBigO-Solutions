T = int(input())

def print_tree(dict, trees, total_tree):
  trees.sort()
  for tree in trees:
    res = (S[tree]/total_tree)*100
    print(tree, '%.4f'%(res))
  

try:
  input()
  for test_case in range(T):
    S = dict();
    trees = []
    total_tree = 0
    while 1:
      tree = input()
      if tree == '':
            break
      total_tree += 1
      if tree in S:
        S[tree] += 1
      else:
        S[tree] = 1
        trees.append(tree)
    print_tree(S, trees, total_tree)
    if test_case < T -1:
      print()
except EOFError:
  print_tree(S, trees, total_tree)  

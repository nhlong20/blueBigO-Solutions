import queue;
def BFS(graph, src, rank):
  q = queue.Queue()
  q.put(src)
  rank[src] = 0
  while not q.empty():
    u = q.get()
    for v in graph[u]:
      if rank[v] == "undefined":
        rank[v] = rank[u] + 1
        q.put(v)
        
def main():
  n = int(input())
  graph = []
  S = dict()
  count = 0

  # build edge list
  for _ in range(n):
    names = input().split()
    ids = []

    # ánh xạ names -> id and add to dict S
    for name in names:
      v = None
      if name in S: v = S[name]
      else:
        S[name] = count
        graph.append([])
        v = count
        count += 1
      ids.append(v)
    
    # Add people in a same team to edge list
    for i in ids:
      for j in ids:
        if i != j: graph[i].append(j)
  
  rank = ["undefined" for _ in range(count)]

  # Build rank array
  if "Isenbaev" in S:
    BFS(graph, S["Isenbaev"], rank)
  # sort name in lexicographically order
  names = []
  for name in S:
    names.append(name)
  names.sort()

  # print result
  for name in names:
    print(name, rank[S[name]])

if __name__ == "__main__":
  main()
        



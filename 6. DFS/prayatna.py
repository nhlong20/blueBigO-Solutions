MAX = 10**5 +5
def DFS(graph, visited, start):
  s = [start]
  visited[start] = True
  while len(s)>0:
    u = s.pop()
    for v in graph[u]:
      if visited[v]: continue
      visited[v] = True
      s.append(v)

    
def test():
  V = int(input()) # 2 <= V <= 10^5
  E = int(input()) # 0 <= E <= N/2
  graph = [[] for _ in range(V)]
  visited = [False]*(V)
  for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  count = 0
  for i in range(V):
    if visited[i]: continue
    count +=1
    DFS(graph, visited, i)

  print(count)



def main():
  T = int(input()) # <= 10
  for _ in range(T):
    test()

if __name__ == '__main__':
  main()
MAX = 2000 + 1
INF = 10**9

graph = []

T = int(input())

def bellmanFord():
  dist = [INF]*MAX
  dist[0] = 0
  for _ in range(n-1):
    for j in range(m):
      v, u, w = graph[j]
      if (dist[v] != INF) and (dist[v] + w < dist[u]):
        dist[u] = dist[v] + w

  for i in range(m):
    v, u, w = graph[i]
    if (dist[v] != INF) and (dist[v] + w < dist[u]):
      return True
  return False 

for _ in range(T):
  n, m = map(int, input().split())
  dist = [INF]*MAX
  graph.clear()

  for _ in range(m):
    x, y, t = map(int,input().split())
    graph.append((x,y,t))
  possible = bellmanFord()
  print(["not possible", "possible"][possible])
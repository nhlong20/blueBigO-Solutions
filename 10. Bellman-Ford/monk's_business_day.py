MAX = 100 + 1
NEG_INF = -10**3+1
T = int(input())

def bellmanFord(n, edges):
  dist = [NEG_INF]*n
  dist[0] = 0
  for _ in range(n-1):
    for v, u, w in edges:
      if dist[v] == NEG_INF: continue
      if dist[u] < dist[v] + w:
        dist[u] = dist[v] + w

  for v, u, w in edges:
    if dist[v] == NEG_INF: continue
    if dist[u] < dist[v] + w:
      return True
  return False 

for _ in range(T):
  n, m = map(int, input().split())
  edges = []

  for k in range(m):
    x, y, t = map(int,input().split())
    edges.append((x-1,y-1,t))

  print(["No", "Yes"][bellmanFord(n, edges)])
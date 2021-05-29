MAX = 1000 +5
dist = [-1]*MAX
graph = [[] for _ in range(MAX)]
visited = [False]*MAX

def DFS(start):
  s = []
  s.append(start)
  visited[start] = True
  dist[start] = 0

  while len(s)>0:
    u = s.pop()
    for v in graph[u]:
      if visited[v]: continue
      visited[v] = True
      dist[v] = dist[u] + 1
      s.append(v)

V = int(input())
E = V - 1

for _ in range(E):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)  

min_dist = MAX
min_id = 0
# determine the distance from the boy to girls
DFS(1)

Q = int(input())
for _ in range(Q):
  girl_id = int(input())
  if dist[girl_id] < min_dist or (dist[girl_id] == min_dist and girl_id < min_id):
    min_dist = dist[girl_id]
    min_id = girl_id

print(min_id)
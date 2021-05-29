import sys
MAX = 10**4 + 5
graph = [[] for _ in range(MAX)]
visited = [False]*MAX
sys.setrecursionlimit(MAX)

def DFS(sr):
  st = []
  st.append(sr)
  visited[sr] = 1
  while len(st) > 0:
    u = st.pop()
    for v in graph[u]:
      if visited[v]: return True
      visited[v] = 1
      st.append(v)
  visited[sr] = 2
  return False
T = int(input())

for t in range(T):
  N, M = map(int, input().split())

  # reset graph and visited
  for i in range(N):
    graph[i].clear()
    visited[i] = False

  for i in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
  
  hasLoop = False

  for i in range(N):
    if visited[i]: continue
    hasLoop = DFS(i)
    if hasLoop: break

  print("YES" if hasLoop else "NO")
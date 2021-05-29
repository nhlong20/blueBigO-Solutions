import queue
EDGE_DISTANCE = 6

def bfs(graph, dist, S):
  q = queue.Queue()
  dist[S] = 0
  q.put(S)

  while not q.empty():
    start = q.get()
    for v in graph[start]:
      if(dist[v] == -1): #if dist = -1 means this vertice has not visted yet
        dist[v] = dist[start] + EDGE_DISTANCE
        q.put(v)
        

def main():
  # step 1: init number of test case
  test_case = int(input())
  for _ in range(test_case):
    # step 2: init number of node and edges and graphs
    N, M = map(int, input().strip().split())
    graphList = [[] for _ in range(N)] 
    
    # Read the edges of the graph by descresing each with one as the node count from 1
    for _ in range(M):
      u, v = map(int, input().strip().split())
      graphList[u-1].append(v-1)
      graphList[v-1].append(u-1)
    # input start vertice
    S = int(input())-1
  
    # init distance array with -1 
    dist = [-1]*N

    #perform BFS to update distance array
    bfs(graphList, dist, S)
    # print distance
    for i in range(N):
      if i != S:
        print(dist[i], end=" ")
    print()


if __name__ == "__main__":
  main()
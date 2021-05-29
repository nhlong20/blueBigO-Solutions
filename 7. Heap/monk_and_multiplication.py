from heapq import *
n = int(input())
arr = list(map(int,input().split()))

heap = []

for i in range(n):
  heappush(heap, -arr[i]) # "-" notation to mark this is max heap
  if i < 2:
    print(-1) 
  else:
    a1 = -heappop(heap)
    a2 = -heappop(heap)
    a3 = -heappop(heap)

    print(a1*a2*a3)
    heappush(heap, -a1)
    heappush(heap, -a2)
    heappush(heap, -a3)
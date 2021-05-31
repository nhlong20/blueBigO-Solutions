import heapq

top_reviews = []
rest_reviews = []
n_reviews = 0
n = int(input())

for _ in range(n):
  line = list(map(int,input().split()))
  opt = line[0]
  if opt == 1:
    val = line[1]
    n_reviews +=1

    if len(top_reviews) > 0 and top_reviews[0] < val:
      heapq.heappush(rest_reviews, -heapq.heappop(top_reviews))
      heapq.heappush(top_reviews, val)
    else:
      heapq.heappush(rest_reviews, -val)
    
    if n_reviews % 3 == 0:
      heapq.heappush(top_reviews, -heapq.heappop(rest_reviews))

  else:
    if len(top_reviews) == 0:
      print("No reviews yet")
    else:
      print(top_reviews[0])
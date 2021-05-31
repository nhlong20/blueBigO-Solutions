import heapq
MAX = 10**6 +5
min_heap = []
max_heap = []
taken = [False]*MAX

def main():
  nth_bills = 0
  total_money = 0
  n = int(input())
  for _ in range(n):
    bills = list(map(int, input().split()))
    for price in bills[1:]:
      nth_bills += 1
      heapq.heappush(min_heap, (price, nth_bills))
      heapq.heappush(max_heap, (-price, nth_bills))
    
    while taken[min_heap[0][1]]:
      heapq.heappop(min_heap)
    while taken[max_heap[0][1]]:
      heapq.heappop(max_heap)

    taken[min_heap[0][1]] = True
    taken[max_heap[0][1]] = True

    total_money += - heapq.heappop(max_heap)[0] - heapq.heappop(min_heap)[0]

  print(total_money)

if __name__ == '__main__':
  main()


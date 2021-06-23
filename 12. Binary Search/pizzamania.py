# I use different way to code, not using binary search
# Time complexity is O(t*n) with t is number of test case
t = int(input());
for _ in range(t):
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  seen = {}
  count = 0
  for i in range(len(arr)):
    remain = m - arr[i]
    if remain in seen: 
      count += 1
      del seen[remain]
    seen[arr[i]] = i
  print(count)
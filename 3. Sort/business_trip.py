k = int(input())
a = list(map(int,input().strip().split()))[:12]
sum = 0
count = 0
if k == 0:
  print(0)
  exit(0)
for el in sorted(a)[::-1]:
  sum +=el
  count +=1
  if sum >= k:
    break
if sum < k:
  print(-1)
else:
  print(count)
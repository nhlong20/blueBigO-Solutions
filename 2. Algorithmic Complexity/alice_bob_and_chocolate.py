n = int(input())
t = list(map(int, input().strip().split()))
i, j = 0, n - 1
s, c = 0, 0
while i <= j:
  if i == j and s <= 0:
    s +=t[i]
    c += 1
    break
  if s > t[j] - t[i]:
    s -= t[j]
    j -= 1
  else:
    s += t[i]
    c += 1
    i +=1
print(c, n - c)
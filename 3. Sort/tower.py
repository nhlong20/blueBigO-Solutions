n = int(input())
a = sorted(map(int,input().strip().split()))
fre = [0]*1001
count = 0
for i in range(n):
  fre[a[i]] +=1
  if fre[a[i]] == 1:
    count +=1
print(max(fre), count)
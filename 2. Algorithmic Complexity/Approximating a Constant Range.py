N = int(input())
A = list(map(int, input().strip().split()))
fre = [0]*(10**5+1)
diff = 0
MAX_DIFF = 1
longest_range = 0
L = R = 0
for i in range(N):
  fre[A[R]] += 1
  if fre[A[R]] == 1:
    diff +=1
  
  while diff > MAX_DIFF+1:  
    if fre[A[L]] == 1:
      diff -=1
    fre[A[L]] -=1
    L +=1
  longest_range = max(longest_range, R-L+1)
  if R < N - 1: R +=1
print(longest_range)
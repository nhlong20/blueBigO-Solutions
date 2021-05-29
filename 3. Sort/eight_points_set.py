nSet = 8
A = []
for _ in range(nSet):
  x, y = map(int, input().strip().split())
  A.append((x,y))

A = sorted(A)
print(['ugly','respectable'][A[0][0] == A[1][0] == A[2][0]
and A[3][0]  == A[4][0]  
and A[5][0]  == A[6][0]  == A[7][0]  
and A[0][1] == A[3][1] == A[5][1]
and A[1][1] == A[6][1]
and A[2][1] == A[4][1] == A[7][1]])

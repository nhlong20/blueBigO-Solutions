n , w = map(int, input().strip().split())
a = sorted(map(int, input().strip().split()))[:2*n]

total_by_gMil = a[0]*n*3
total_by_mMil = a[n]*n*3/2

res = min(w,total_by_gMil, total_by_mMil )
print(res)
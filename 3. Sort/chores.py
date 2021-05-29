n, a, b = map(int, input().strip().split())
H = sorted(map(int,input().strip().split()))
print(H[n-a] - H[n-a-1])
n, k = map(int, input().split())
a = sorted(len(input()) for _ in range(n))
pwd = len(input())

t = a.index(pwd) # find index of pwd'slengh in the list a
b= t+a.count(pwd) # n times which
a = t 
print(1+a+a//k*5,b+((b-1)//k)*5)
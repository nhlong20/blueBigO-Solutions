class Solution:
  def __init__(self) -> None:
      self.rate = ["Good", "Bad", "Average"]
  def solve(self):
    T = int(input())
    for _ in range(T):
      n ,x = map(int, input().split())
      s = set()
      for el in list(map(int, input().split())):
        s.add(el)
      if len(s) == x: print(self.rate[0])
      if len(s) > x: print(self.rate[2])
      if len(s) < x: print(self.rate[1])

Solution().solve()
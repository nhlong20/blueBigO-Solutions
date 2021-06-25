S = input()
T = input()
countS = [0]*52
countT = [0]*52
ansY = ansW = 0

# util function to get index of a character in range 0 -> 52, 
def getIdx(c):
  idx = -1
  if c >= 'a': idx = ord(c) - 97 + 26
  elif c <= 'Z': idx = ord(c) - 65
  return idx

# count frequency of a single char in S
for c in S:
  idx = getIdx(c)
  countS[idx] += 1
# count frequency of a single char in T
for c in T:
  idx = getIdx(c)
  countT[idx] += 1

# count "YAY"
cntY = 0
for c in range(52):
  cntY = min(countS[c], countT[c])
  ansY += cntY
  countS[c] -= cntY
  countT[c] -= cntY

# count "WHOOPS"
cntW = 0
for c in range(26):
  cntW = min(countS[c], countT[c+26]) + min(countS[c+26], countT[c])
  ansW += cntW

print(ansY, ansW)
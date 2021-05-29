n = int(input())

for _ in range(n):
  s = input()
  st = []
  count = 0
  state = 1
  for ch in s:
    if ch == "<":
      st.append(ch)
      count +=1
    elif ch == ">" and len(st) != 0:
      st.pop()
    else: 
      state = 0
      break
  if len(st) == 0 and state == 1:
    print(2*count)
  else:
    print(0)
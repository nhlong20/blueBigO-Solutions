val = {
  "H": 1,
  "C": 12,
  "O": 16,
  ")": -1,
  "(": 0
}

exp = input()
st = []
for el in exp:
  if el == '(':
    st.append(val[el])
  elif el == ")":
    v = val[el]; total = 0
    # loop to get all value between two parenthesis
    while v!= val['(']:
      v = st.pop()
      total += v
    st.append(total)
  elif el == 'H' or el == 'C' or el == 'O':
    st.append(val[el])
  else: # if there a number after the atom
    v = st.pop()
    st.append(v*(ord(el)-ord("0")))

res = 0
while len(st) != 0:
  res += st.pop()

print(res)
  
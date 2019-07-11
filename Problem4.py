l = 0
for x in range(0, 900, 1):
  for y in range(0, 900, 1):
    m = 999 - x
    n = 999 - y
    forward = str(m * n)
    backward = forward[::-1]
    if forward == backward:
      if int(forward) > l:
        l = int(forward)
print(l)
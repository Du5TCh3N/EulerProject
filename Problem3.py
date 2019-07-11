x = 600851475143
for i in range(1, x, 1):
  if x % i == 0:
    prime = True
    for n in range(2, i, 1):
      if i % n == 0:
        prime = False
    if prime:
      print(i)
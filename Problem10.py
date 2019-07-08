# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

#Standard Slow Method
'''
def prime(x):
    for i in range (2, x):
        if (x % i) == 0:
            return False

sum = 0

for i in range(2, 2000000):
    if (prime(i) != False):
        print(i)
        sum += i

print(sum)
'''

#Sieve of Eratosthenes
#1. Create a list l of consecutive integers {2,3,…,N}.
#2. Select p as the first prime number in the list, p=2.
#3. Remove all multiples of p from the l.
#4. set p equal to the next integer in l which has not been removed.
#5. Repeat steps 3 and 4 until p2 > N, all the remaining numbers in the list are primes
N = 2000000

l = list(range(2, N))

p = 2
index = 0

while p * p < N:
    for i in l:
        if (i > p) and (i % p == 0):
            l.remove(i)
    if index != len(l) - 1:
        index += 1
        p = l[index]
    else:
        break

print(sum(l))

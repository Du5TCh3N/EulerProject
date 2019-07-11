FibonacciNumbers = [1, 1]
n = 0
while n <= 999:
    x = FibonacciNumbers[len(FibonacciNumbers) - 1] + FibonacciNumbers[len(FibonacciNumbers) - 2]
    FibonacciNumbers.append(x)
    n = len(str(x))

print(len(str(x)), len(FibonacciNumbers))

import math

a = int(input())

for i in range(a):
    n, m = map(int, input().split())
    result = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(result)

n = int(input())
l = []

for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    l.append((a,b))

l.sort(key=lambda parameter_list : parameter_list[0])

for i in l:
    print(i[0], i[1])

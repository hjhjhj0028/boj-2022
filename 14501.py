n = int(input()) # 남은 날짜

t = [] # 소요시간
p = [] # 페이

for i in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)

p.append(0)
#print("소요시간 ", t)
#print("페이 ", p)
#print()

for i in reversed(range(n)):
  #print("now i is ", i)
  #print("t[i] + i is {} + {}" .format(t[i], i))

  if (t[i] + i > n):
    p[i] = p[i + 1]
    #print("p[i] is ", p[i])
    #print(p)
    #print()
  else:
    p[i] = max(p[i+1], p[i] + p[i+t[i]])
    #print("p[i] is ", p[i])
    #print(p)
    #print()

print(p[0])

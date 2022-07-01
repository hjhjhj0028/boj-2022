total = set(range(1, 10001))
new = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    new.add(i)
    
selfnum = sorted(total-new)
for i in selfnum:
    print(i)

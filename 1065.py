n = int(input())
hansu = 0

for i in range(1, n+1):
    if i<100:
        hansu += 1
    else:
        n_str = list(map(int, str(i)))
        if n_str[2] - n_str[1] == n_str[1] - n_str[0]:
            hansu += 1
print(hansu)

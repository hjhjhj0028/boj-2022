import heapq, sys

n = int(sys.stdin.readline())
maxh, minh = [], []

for i in range(n):
    num = int(sys.stdin.readline())
    if len(maxh) == len(minh):
        heapq.heappush(maxh, (-1 * num))
    else:
        heapq.heappush(minh, num)
    if len(minh) > 0 and minh[0] < (maxh[0]*-1):
        tmp1 = heapq.heappop(minh)
        tmp2 = heapq.heappop(maxh)*(-1)
        heapq.heappush(maxh, (-1 * tmp1))
        heapq.heappush(minh, tmp2)

    print(maxh[0]*-1)

from sys import stdin
from collections import deque
t = stdin.readline().strip()
j = 0
while t != '0 0':
    tmp = t.split(' ')
    P, C = int(tmp[0]), int(tmp[1])
    print('Case ' + str(j+1) + ':')
    q = deque(range(1, min(P+1, C+1)))
    for _ in range(C):
        tmp = stdin.readline().strip()
        if len(tmp) == 1:  # N
            x = q.popleft()
            print(x)
            q.append(x)
        else:  # E x
            x = int(tmp[1:])
            if x in q:
                q.remove(x)
            q.appendleft(x)
    t = stdin.readline().strip()
    j += 1
import sys
i=0
for t in sys.stdin:
    if i%2 == 0:
        n=t[0]
    else:
        print(t.count(n))
    i+=1







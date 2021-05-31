import sys
while 1:
    t=sys.stdin.readline()
    if not t:
        break
    W=int(t)
    N=int(sys.stdin.readline())
    s=0
    for _ in range(N):
        a,b=sys.stdin.readline().strip().split(' ')
        w,l=int(a),int(b)
        s+=w*l
    print(s//W)

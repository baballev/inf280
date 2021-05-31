from sys import stdin
PI = 3.141592653590

def compute_radius(i):
    min_r = 2*max(box[1][0], box[1][1], box[1][2])

    min_r = min(abs(balloons[i][0] - box[0][0]), min_r)
    min_r = min(abs(balloons[i][0] - box[1][0]), min_r)
    min_r = min(abs(balloons[i][1] - box[0][1]), min_r)
    min_r = min(abs(balloons[i][1] - box[1][1]), min_r)
    min_r = min(abs(balloons[i][2] - box[0][2]), min_r)
    min_r = min(abs(balloons[i][2] - box[1][2]), min_r)

    for k in range(n):
        if k != i and visited[k]:
            min_r = min(((balloons[i][0]-balloons[k][0])**2+(balloons[i][1]-balloons[k][1])**2+(balloons[i][2]-balloons[k][2])**2)**0.5 - balloons[k][3], min_r)

    return min_r

def gonfle(j, curr_vol, vol):
    if j == n:
        if curr_vol > vol:
            vol = curr_vol
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                balloons[i][3] = compute_radius(i)
                if balloons[i][3] > 0:
                    gonfle(j+1, curr_vol + (4/3)*PI*balloons[i][3]**3, vol)
                else:
                    gonfle(j+1, curr_vol, vol)
                visited[i] = False

i_box = 0
while 1:
    t = stdin.readline()
    if not t:
        break
    if t.strip() == '0':
        t = stdin.readline().strip()

    n = int(t)
    i_box += 1
    vol = 0.0

    x, y, z = stdin.readline().strip().split(' ')
    box = []
    box.append((int(x), int(y), int(z)))
    x, y, z = stdin.readline().strip().split(' ')
    box.append((int(x), int(y), int(z)))
    Vbox = abs(box[0][0] - box[1][0])*abs(box[0][1] - box[1][1])*abs(box[0][2] - box[1][2])
    balloons = []
    for i in range(n):
        x, y, z = stdin.readline().strip().split(' ')
        balloons.append([int(x), int(y), int(z), 0])

    visited = [False for _ in range(n)]  # Is balloon placed at point i
    gonfle(0, 0.0, vol)

    print("Box " + str(i_box) + ": " + str(int(Vbox - vol)))
    print("")
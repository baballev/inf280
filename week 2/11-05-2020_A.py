from sys import stdin
from collections import deque
test_n = int(stdin.readline().strip())
def solve(cargo, stock, curr_cap):
    if stock:
        x, y, w = stock.popleft()
    else:  # Cas de base
        livraison = 0
        prev_x, prev_y = 0, 0
        while cargo:
            next_x, next_y = cargo.pop()
            livraison += abs(next_x - prev_x) + abs(next_y - prev_y)
            prev_x, prev_y = next_x, next_y
        livraison += prev_x + prev_y
        return livraison

    if curr_cap - w >= 0:
        new_cargo = cargo.copy()
        new_cargo.append((x, y))
        d1 = solve(new_cargo, stock, curr_cap-w)  # left tree
        livraison = 0
        prev_x, prev_y = 0, 0
        while cargo:
            next_x, next_y = cargo.pop()
            livraison += abs(next_x - prev_x) + abs(next_y - prev_y)
            prev_x, prev_y = next_x, next_y
        livraison += prev_x + prev_y
        d2 = livraison + solve(cargo.copy(), stock, curr_cap-w)  # right tree
        d = min(d1, d2)
    else:
        livraison = 0
        prev_x, prev_y = 0, 0
        while cargo:
            next_x, next_y = cargo.pop()
            livraison += abs(next_x - prev_x) + abs(next_y - prev_y)
            prev_x, prev_y = next_x, next_y
        livraison += prev_x + prev_y
        new_cargo = cargo.copy()
        new_cargo.append((x,y))
        d = livraison + solve(new_cargo, stock, C)
    return d

for _ in range(test_n):
    stdin.readline()  # Blank line
    C = int(stdin.readline().strip())
    N = int(stdin.readline().strip())
    stock = deque()
    s = 0
    curr_x, curr_y = 0, 0  # stock's coordinates
    for _ in range(N):  # Read all items to be delivered
        x, y, w = stdin.readline().strip().split(" ")
        x, y, w = int(x), int(y), int(w)
        stock.append((x, y, w))
    cargo = deque()
    print(solve(cargo, stock, C))
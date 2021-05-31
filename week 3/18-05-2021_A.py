## Basically, consist in implementing Floyd-Warshall
from sys import stdin

network_n = 0
while 1:
    network_n += 1
    t = stdin.readline().strip()
    if t == '0 0':
        break

    P, R = int(t.split()[0]), int(t.split()[1])
    adjacency_lists = [[] for _ in range(P)]
    n_to_idx = {}
    idx = 0
    edge_counter = 0
    for _ in range(R):  # Building graph with adjacency lists
        if edge_counter >= R:
            break
        t = stdin.readline().strip().split()
        for i in range(len(t)//2):
            n1, n2 = t[2*i].strip(), t[2*i+1].strip()
            if n1 not in n_to_idx.keys():
                n_to_idx[n1] = idx
                idx += 1
            if n2 not in n_to_idx.keys():
                n_to_idx[n2] = idx
                idx += 1
            adjacency_lists[n_to_idx[n1]].append(n_to_idx[n2])
            adjacency_lists[n_to_idx[n2]].append(n_to_idx[n1])
            edge_counter += 1

    MAX = P**4
    # Floyd-Warshall
    dist = [[MAX]*P for _ in range(P)]
    for u in range(P):
        dist[u][u] = 0
        for tmp in adjacency_lists[u]:
            dist[u][tmp] = 1
    for k in range(P):
        for i in range(P):
            for j in range(P):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    sol = 0
    for i in range(P):
        for j in range(i+1, P):
            sol = max(dist[i][j], sol)

    if sol == MAX:
        print('Network ' + str(network_n) + ': DISCONNECTED')
    else:
        print('Network ' + str(network_n) + ': ' + str(sol))
    print('')

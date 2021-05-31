# Build a graph with molecules affinity sites and then find if there's a cycle using DFS
from sys import stdin
t = stdin.readline().strip()

def invert(c):
    if c == '+':
        return '-'
    elif c == '-':
        return '+'
    else:
        return '0'

'''
def dfs2():
    visited = {k: False for k in adjacency_lists.keys()}
    on_stack = {k: False for k in adjacency_lists.keys()}
    stack = []

    for node in adjacency_lists.keys():
        if visited[node]:
            continue
        stack.append(node)
        while len(stack) > 0:
            curr_node = stack[-1]
            if not visited[curr_node]:
                visited[curr_node] = True
                on_stack[curr_node] = True
            else:
                on_stack[curr_node] = False
                stack.pop()

            for neigh in #NOT FINISHED
    return False
'''


def dfs(node, visited, stack):
    visited[node] = True
    stack[node] = True
    for neighb in adjacency_lists[node]:
        if not visited[neighb]:
            if dfs(neighb, visited, stack):
                return True
        elif stack[neighb]:
            return True
    stack[node] = False
    return False

while t:
    n = int(t)
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    adjacency_lists = {}
    for letter in alph:
        adjacency_lists[letter + '-'] = []
        adjacency_lists[letter + '+'] = []

    mols = stdin.readline().strip().split()
    for mol1 in mols:
        for i in range(4):
            aff = mol1[2*i:2*i+2]
            if aff == '00':
                continue
            adjacency_lists[aff].extend([mol1[2*j] + invert(mol1[2*j+1]) for j in range(4) if mol1[2*j] != '0' and j != i])
    for key in adjacency_lists.keys():
        adjacency_lists[key] = set(adjacency_lists[key])

    visited = {k : False for k in adjacency_lists.keys()}
    stack = {k : False for k in adjacency_lists.keys()}
    cycle = False

    for node in adjacency_lists.keys():
        if not visited[node]:
            if dfs(node, visited, stack):
                cycle = True

    if cycle:
        print("unbounded")
    else:
        print("bounded")
    t = stdin.readline().strip()

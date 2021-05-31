#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>
#include <iterator>
#define PI 3.141592653590

using namespace std;

// Basically, find eulerian cycle in the graph.
// First, do union find to find the connected components in the color graph.
// if there is more than one connected components, then some beads have been lost.
// else, use the eulerian cycle property with the number of nodes: If every edge -> even degree, won else lost
// Use DFS to find a feasible necklace
int UF_table[50];
int ranking[50];
int color_graph[50][50];

void DFS(int root) {
    for (int k = 0; k < 50; k++) {
        if (color_graph[root][k] > 0) {
            color_graph[root][k]--;
            color_graph[k][root]--;
            DFS(k);
            cout << k << " " << root << endl;
        }
    }
}
int Find(int i) { // Climb the node's set tree recursively until you reach the root by using the T table
    if (UF_table[i] == i) {
        return i;
    }
    else {
        return UF_table[i] = Find(UF_table[i]);
    }
}
void Union(int i, int j) { // Merge two sets together
    i = Find(i);
    j = Find(j);
    if (i != j) {
        if (ranking[i] > ranking[j]) {
            ranking[i] = ranking[i] + ranking[j];
            UF_table[j] = i;
        }
        else {
            ranking[j] = ranking[j] + ranking[i];
            UF_table[i] = j;
        }
    }
}


int main()
{
    int T, N, x, y;

    cin >> T;
    for (int i = 0; i < T; i++) {
        map<int, int> degrees;
        // INIT GRAPH AND 
        for (int k = 0; k < 50; k++) {  // Init Union-Find Table
            UF_table[k] = k;
            ranking[k] = 1;
        }
        for (int k1 = 0; k1 < 50; k1++) { // Init Graph
            for (int k2 = 0; k2 < 50; k2++) {
                color_graph[k1][k2] = 0;
            }
        }

        cin >> N;

        for (int j = 0; j < N; j++) { // Build Graph
            cin >> x >> y;
            color_graph[x][y]++;
            color_graph[y][x]++;
            
            degrees[x]++;
            degrees[y]++;
            Union(x, y);
        }
        // CHECK IF THERE MORE THAN ONE CONNECTED COMPONENTS / IF THERE ARE NODES WITH ODD DEGREE
        bool flag = true;
        bool first = true;
        int previous = 0;
        map<int, int>::iterator it;    
        for(it=degrees.begin(); it!=degrees.end();it++) { // Iterate over all nodes with degree > 0 (i.e which appeared in the input)
            int key = it->first;
            int value = it->second;
            if (first) {
                first = false;
                previous = Find(key);
            }
            else if (Find(key) != previous) {
                flag = false;
                break;
            }
            if (value % 2 != 0) {
                flag = false;
                break;
            }
            }

        cout << "Case #" << i + 1 << endl;
        if (flag) {  // If the eulerian cycle exists, DFS to get a necklace
            int root = degrees.begin()->first;
            DFS(root);
        }
        else {
            cout << "some beads may be lost" << endl;
        }
        cout << endl;
        
    }


}
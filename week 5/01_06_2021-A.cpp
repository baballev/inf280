#include <iostream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <list>
#include <stack>
#include <queue>
#define PI 3.141592653590
using namespace std;

#define max_nodes 21;


void BFS() {
    queue<unsigned long> q;
    q.push((unsigned long)(1 << n) - 1);  // Init all nodes to be explored in BFS
    
    // Enumerate all sets

    for (int i = 0; i < n; i++) {

    }




}



int main()
{
    unsigned long graph[max_nodes]; // 32 bits
    unsigned long x, y;
    int n, m;


    while (true) { // handle multiple test cases
        cin >> n >> m;
        if (n == 0 && m == 0) {
            break;
        }
        for (int i = 0; i < n; i++) {
            graph[i] = (unsigned long) 0;
        }
        for (int i = 0; i < m; l i++) {
            cin >> x >> y;
            graph[x] = graph[x] | (1 << y); // Get the bit corresponding to y and add it to the graph
            graph[y] = graph[y] | (1 << x);
        }


        BFS();
    }
}
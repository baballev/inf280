#include <iostream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#define PI 3.141592653590
using namespace std;

// Use Union-Find to check whether the latest binding pair in the sequence is in the same set. 
// If not, union the two compounds of the binding pair
// If they belong in the same set, refuse the binding pair

// Union-Find code adapted from https://youtu.be/0jNmHPfA_yE

#define n_compounds 100000

int T[n_compounds]; // Size ~ 10**5 * 4B ~ 40 kB << 256 MB

int Find(int i) { // Climb the node's set tree recursively until you reach the root by using the T table
    if (T[i] == i) {
        return i;
    }
    else {
        return Find(T[i]);
    }
}
void Union(int i, int j) { // Merge two sets together
    T[Find(i)] = Find(j);
}

int main()
{

    int A, B;
    int refusals;

    while (cin >> A) { // handle multiple test cases
        refusals = 0; // init counter
        for (int i = 0; i < n_compounds; i++) {
            T[i] = i;  // Init Union-Find table
        }
        while (A != -1 && cin >> B) {
            if (Find(T[A]) == Find(T[B])) {
                refusals++;
            }
            else {
                Union(A, B);
            }
            cin >> A;
        }
        cout << refusals << endl;
    }
}
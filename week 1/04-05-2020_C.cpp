#include <iostream>
#include <string.h>
#include <deque>
using namespace std;

int main() {
    int P;
    int C;
    int j = 0;
    int x;
    string s;
    deque<int> q;
    while(cin >> P >> C){
      if (not (P == 0 && C ==0)){
      cout << "Case " << j+1 << ":" << endl;
      }
      q.clear();
      for(int i=0; i<P; i++){
        q.push_back(i+1);
      }

      for(int i = 0; i < C; i++){
        cin >> s;
        if (s == "N"){
          int t = q.front();
          cout << t << endl;
          q.pop_front();
          q.push_back(t);

        } else {
          cin >> x;
          for (deque<int>::const_iterator it= q.begin(), itend =q.end(); it!=itend; ++it){
            if(*it == x){
              q.erase(it);
              break;
            }
          }
          q.push_front(x);
        }
      }
      j++;
    }
}

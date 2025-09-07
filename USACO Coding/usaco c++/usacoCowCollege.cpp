#include <bits/stdc++.h>

using namespace std;


int main() {
  long long int n, maxTuition=0, maxtot=0;
  cin >> n;
  
  vector<long long int> pay(n);
  
  for (int i = 0; i < n; i++) {
     cin >> pay[i];
     }
    
    sort(pay.begin(), pay.end());
  for(int i = 0; i < n; i++){
    if(maxtot < pay[i] * (n - i)){
        maxtot = pay[i] * (n-i);
        maxTuition = pay[i];
    }
  }
  cout << maxtot << " " << maxTuition;
}

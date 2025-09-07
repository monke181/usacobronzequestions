#include <bits/stdc++.h>

using namespace std;

int main()
{
    //USACO 2018 February Contest, Bronze Problem 1. Teleportation http://usaco.org/index.php?page=viewproblem2&cpid=807
    freopen("teleport.in", "r", stdin);
    freopen("teleport.out", "w", stdout);
    long long int a, b, x, y;
    cin >> a >> b >> x >> y;
    
    long long dist = abs(min(x,y)-min(a,b))+abs(max(x,y)-max(a,b));
    cout << min(abs(a-b), dist);
}
#include <bits/stdc++.h>

using namespace std;

int main()
{
   freopen("square.in", "r", stdin);
   freopen("square.out", "w", stdout);


    long long int x1a, y1a, x1b,y1b,x2a,y2a,x2b,y2b, area=0;
    cin >> x1a >> y1a >> x2a >> y2a >> x1b >> y1b >> x2b >> y2b;
    
    long long minx= min(x1a, x1b);
    long long maxx = max(x2a, x2b);
    long long miny= min(y1a, y1b);
    long long maxy = max(y2a, y2b);
    
    long long side = max((maxx-minx), (maxy-miny));
    cout<<side*side;
}
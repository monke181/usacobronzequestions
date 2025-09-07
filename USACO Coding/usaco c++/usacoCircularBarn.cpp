#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("cbarn.in", "r", stdin);
	freopen("cbarn.out", "w", stdout);

	long long int n, temp, sum=0, minim = INT_MAX, k;
	vector<int> v;
	cin >> n;
	for (int i=0; i<n; i++) {
		cin >> temp;
		v.push_back(temp);
	}
	for(int start = 0; start<n; start++) {
	    sum = 0;
	    k = start;
		for(int j =0; j < n; j++) {
			sum += v[k % n]*j;
			k++;
		}
		minim = min(minim, sum);
	}
    cout << minim;
}
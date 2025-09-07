#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("speeding.in", "r", stdin);
	freopen("speeding.out", "w", stdout);

	int N, M;
	int length, speed;
	cin >> N >> M;

	vector<int> limit;

	for(int i =0; i< N; i++) {
		cin >> length >> speed;
		for(int j = 0; j<length; j++) {
			limit.push_back(speed);
		}
	}

	vector<int> Bessie;

	for(int i =0; i< M; i++) {
		cin >> length >> speed;
		for(int j = 0; j<length; j++) {
			Bessie.push_back(speed);
		}
	}
	int highest=0;
	for(int i =0; i < 100; i++) {
        highest = max(highest, Bessie[i]-limit[i]);
	}
	cout << highest;
}

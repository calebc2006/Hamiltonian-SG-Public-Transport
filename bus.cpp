#include <iostream>
#include <vector>
#include <queue>
using namespace std;
typedef pair<int, int> pii;

int stops[4] = {
    17141, // Clementi Stadium
    42299, // Aft Toh Tuck Cres
    97041, // Ballota Park Condo
    70051, // Aft Joo Seng Rd
};

vector<int> busAdjList[100000];
queue<int> q;
int dist[100000][100000];
bool vis[100000];

void bfs(int start) {
    for (int i=0; i<100000; i++) {
        dist[start][i] = 1e9;
        vis[i] = false;
    }
        
    q.push(start);
    vis[start] = true;
    dist[start][start] = 0;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        vis[cur] = true;

        for (auto it : busAdjList[cur]) {
            if (!vis[it]) q.push(it); 
            dist[start][it] = min(dist[start][it], dist[start][cur] + 1);
        }
    }
}

int main() {
    int n = 51;
    switch (n) {
        case
    }
}


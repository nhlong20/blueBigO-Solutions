#include <bits/stdc++.h>

using namespace std;

const int MAX = 250 + 5;
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, 1, -1};
bool visited[MAX][MAX];
int images[MAX][MAX];
int slickFre[MAX*MAX];
int main(){
  while(1){
    int N, M;
    cin >> N >> M;
    if(N == 0 || M == 0) break;
    // MxN matrix of False values to track visited nodes at [i,j]
    for (int i = 0; i < N; i++){
      for (int j = 0; j < M; j++){
        visited[i][j] = false;
      }
    }
    for (int i = 0; i <= M*N; i++){
        slickFre[i] = 0;
    }
    for (int i = 0; i < N; i++){
      for (int j = 0; j < M; j++){
        cin >> images[i][j];
      }
    }
  
    queue<int> rq;
    queue<int> cq;
    int total = 0;
    for (int i = 0; i < N; i++){
      for (int j = 0; j < M; j++){
        if(visited[i][j]) continue;
        if(!images[i][j]) continue;
        visited[i][j] = true;
        rq.push(i); cq.push(j);
        int move_count = 1;
        while(!rq.empty()){
          int r = rq.front(); rq.pop();
          int c = cq.front(); cq.pop();
          for(int k =0;k<4;k++){
            int rr = r + dr[k];
            int cc = c + dc[k];
            // Skip out of bounds location
            if(rr < 0 || cc < 0) continue;
            if(rr >= N || cc >= M) continue;
            //skip visited location and blocked cells
            if(visited[rr][cc]) continue;
            if(images[rr][cc] == 0) continue;

            move_count ++;
            visited[rr][cc] = true;
            rq.push(rr); cq.push(cc);
          }
        }
        slickFre[move_count]++;
        total ++;
      }
    }
    cout << total << endl;
    for(int i = 0; i<= N*M; i++){
      if(slickFre[i] != 0){
        cout << i << " " << slickFre[i] <<endl;
      }
    }
  }
}
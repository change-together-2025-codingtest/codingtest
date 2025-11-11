import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        boolean[] visited = new boolean[n];
        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {      // 아직 방문하지 않은 컴퓨터라면
                dfs(i, computers, visited, n);
                answer++;           // 새로운 네트워크 발견
            }
        }
        return answer;
    }

    void dfs(int node, int[][] computers, boolean[] visited, int n) {
        visited[node] = true;

        for (int j = 0; j < n; j++) {
            // 자기 자신이 아니고, 연결되어 있으며, 아직 방문 안 했으면
            if (j != node && computers[node][j] == 1 && !visited[j]) {
                dfs(j, computers, visited, n);
            }
        }
    }
}

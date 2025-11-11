import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        boolean[] visited = new boolean[n];
        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(i, computers, visited, n);
                answer++;
            }
        }
        return answer;
    }

    void bfs(int start, int[][] computers, boolean[] visited, int n) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();

            for (int j = 0; j < n; j++) {
                if (j != node && computers[node][j] == 1 && !visited[j]) {
                    queue.add(j);
                    visited[j] = true;
                }
            }
        }
    }
}

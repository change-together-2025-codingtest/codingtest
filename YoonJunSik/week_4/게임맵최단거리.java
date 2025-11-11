import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;        // 행
        int m = maps[0].length;     // 열
        boolean[][] visited = new boolean[n][m];// 방문 여부 체크 배열

        // 방향 벡터 (상, 하, 좌, 우)
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        // BFS 큐 선언: (x, y, 거리)
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0,0,1});
        visited[0][0] = true;

        while(!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int dist = current[2];

            // 상대 팀 진영 (n-1, m-1)에 도착한 경우
            if(x == n - 1 && y == m - 1) {
                return dist;
            }

            // 상하좌우 탐색
            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 맵 범위 벗어나면 패스
                if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                // 벽이거나 이미 방문한 곳이면 패스
                if(maps[nx][ny] == 0 || visited[nx][ny]) continue;

                // 이동 가능한 칸이면 큐에 추가
                visited[nx][ny] = true;
                queue.add(new int[]{nx, ny, dist + 1});
            }
        }
        return -1;
    }
}

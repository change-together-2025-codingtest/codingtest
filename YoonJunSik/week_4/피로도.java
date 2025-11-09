import java.util.*;

class Solution {
    int max = 0;

    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        dfs(k,dungeons,visited,0);
        return max;
    }

    private void dfs(int fatigue, int[][] dungeons, boolean[] visited, int count) {
        //fatigue는 현재 피로도를 dungeons는 던전 정보를, visited는 방문여부를, count는 방문한 던전 개수를 저장
        max = Math.max(max, count);// max와 count 중 큰 것을 반환

        for(int i=0; i< dungeons.length; i++) {
            int required = dungeons[i][0]; // 최소 필요 피로도
            int consume = dungeons[i][1]; // 소모 필요도

            if(!visited[i] && fatigue >= required) {
                visited[i] = true;
                dfs(fatigue - consume, dungeons, visited, count + 1);
                visited[i] = false;
            }
        }
    }
}
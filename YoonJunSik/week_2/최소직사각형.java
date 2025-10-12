import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int maxW = 0;  // 가로의 최대값
        int maxH = 0;  // 세로의 최대값

        for (int i = 0; i < sizes.length; i++) {
            // 각 명함을 회전시켜서 가로가 더 크도록 정렬
            int w = Math.max(sizes[i][0], sizes[i][1]);
            int h = Math.min(sizes[i][0], sizes[i][1]);

            // 가로, 세로 중 최대값 갱신
            maxW = Math.max(maxW, w);
            maxH = Math.max(maxH, h);
        }

        // 결과 = 최대 가로 * 최대 세로
        return maxW * maxH;
    }
}

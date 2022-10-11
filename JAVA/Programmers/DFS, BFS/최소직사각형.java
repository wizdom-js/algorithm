class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int width = 0;
        int height = 0;
        for (int[] size : sizes) {
            // 길이가 더 긴 곳을 세로로 배치 은
            // => 짧은 길이는 짧 길이 끼리, 긴 길이는 긴 길이 끼리 비교
            int w;
            int h;
            if (size[0] < size[1]) {
                w = size[0];
                h = size[1];
            } else {
                w = size[1];
                h = size[0];
            }

            width = Math.max(width, w);
            height = Math.max(height, h);
        }

        answer = width * height;
        return answer;
    }
}
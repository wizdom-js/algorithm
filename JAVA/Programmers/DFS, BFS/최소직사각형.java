class Solution {
    public int solution(int[][] sizes) {
        int width = 0;
        int height = 0;
        for (int[] size : sizes) {
            // 길이가 더 긴 곳을 세로로 배치하기
            // => 짧은 길이는 짧 길이 끼리, 긴 길이는 긴 길이 끼리 비교
            width = Math.max(width, Math.min(size[0], size[1]));
            height = Math.max(height, Math.max(size[0], size[1]));
        }

        int answer = width * height;
        return answer;
    }
}
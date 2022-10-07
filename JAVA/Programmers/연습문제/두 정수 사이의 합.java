class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        // a, b 대소 정해져 있지 않음
        for (int i = (a < b ? a : b); i <= (a < b ? b : a); i++) {
            answer += i;
        }
        return answer;
    }
}
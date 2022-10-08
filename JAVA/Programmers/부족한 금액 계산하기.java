class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        for (int n = 1; n <= count; n++) {
            answer += price * n;
        }

        answer -= money;
        answer = answer < 0 ? 0 : answer;

        return answer;
    }
}
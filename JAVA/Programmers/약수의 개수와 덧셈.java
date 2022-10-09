class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int n = left; n < right + 1; n++) {
            if (getDivisorN(n) % 2 == 0) answer += n;
            else answer -= n;
        }
        return answer;
    }

    public int getDivisorN(int n) {
        int count = 0;
        for (int i = 1; i <= (n / 2) + 1; i++) {
            if (i * i == n) count++;
            else if (n % i == 0) count += 2;
        }
        return count;
    }
}


// 제곱수를 이용한 풀이
class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int n = left; n < right + 1; n++) {
            // 제곱수이면 약수의 개수는 홀수
            if (n % Math.sqrt(n) == 0) answer -= n;
            else answer += n;
        }
        return answer;
    }
}
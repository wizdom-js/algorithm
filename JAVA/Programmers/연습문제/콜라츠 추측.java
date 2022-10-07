class Solution {
    public int solution(int num) {
        int answer = 0;
        long n = num;   // 계산 중 int 자료형의 범위를 넘을 수 있으므로
        while (n != 1 && answer < 500) {
            answer ++;
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n *= 3;
                n ++;
            }
        }

        answer = answer == 500 ? -1 : answer;
        return answer;
    }
}

class Solution {
    public int solution(int num) {
        long n = num;   // 계산 중 int 자료형의 범위를 넘을 수 있으므로
        for (int answer = 0; answer < 500; answer++){
            if (n == 1) return answer;
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = n * 3 + 1;
            }
        }
        return -1;
    }
}
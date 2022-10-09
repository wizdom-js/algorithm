class Solution {
    public int[] solution(int n, int m) {
        int gcd = n < m ? getGCD(m, n) : getGCD(n, m);  // 최대공약수
        int lcm = n * m / gcd;  // 최소공배수

        int[] answer = {gcd, lcm};
        return answer;
    }

    public int getGCD(int a, int b) {
        // 유클리드 호제법
        while (a % b != 0) {
            int tmp = b;
            b = a % b;
            a = tmp;
        }
        return b;
    }
}
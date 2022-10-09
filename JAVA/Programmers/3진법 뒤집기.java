class Solution {
    public int solution(int n) {
        int answer = Integer.parseInt(reverseTernary(n), 3);
        return answer;
    }
    
    public String reverseTernary(int n) {
        StringBuilder ternary = new StringBuilder();
        while (n > 0) {
            ternary.insert(0, n % 3);
            n /= 3;
        }
        return ternary.reverse().toString();
    }
}
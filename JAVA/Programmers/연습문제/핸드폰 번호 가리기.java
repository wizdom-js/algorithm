class Solution {
    public String solution(String phone_number) {
        int phone_length = phone_number.length();
        String answer = "*".repeat(phone_length - 4);
        answer += phone_number.substring(phone_length - 4);
        return answer;
    }
}
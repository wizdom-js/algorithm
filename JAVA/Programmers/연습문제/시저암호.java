class Solution {
    public String solution(String s, int n) {
        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            int charNumber = (int)s.charAt(i);  // 아스키코드로 변환
            if (charNumber == 32) { // 공백
                answer.append(" ");
            } else {    // 문자
                int startAscii = charNumber <= 90 ? 64 : 96;
                int endAscii = charNumber <= 90 ? 90 : 122;
                charNumber += n;

                // z 또는 Z를 넘었을 경우
                if (charNumber > endAscii) {
                    charNumber = startAscii + (charNumber - endAscii);
                }
                answer.append((char)(charNumber));
            }

        }
        return answer.toString();
    }
}
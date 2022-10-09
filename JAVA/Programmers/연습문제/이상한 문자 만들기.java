class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        int idx = 0;
        for (int i = 0; i < s.length(); i++) {
            String alphabet = s.substring(i, i+1);

            if (alphabet.isBlank()) {
                idx = 0;
            } else {
                if (idx % 2 == 0)  {
                    alphabet = alphabet.toUpperCase();
                } else {
                    alphabet = alphabet.toLowerCase();
                }
                idx++;
            }
            answer.append(alphabet);
        }

        return answer.toString();
    }
}
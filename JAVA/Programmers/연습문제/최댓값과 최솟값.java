class Solution {
    public String solution(String s) {
        int maxNum = -1000000000;
        int minNum = 100000000;
        StringBuilder tmpNum = new StringBuilder();
        for(int i=0; i < s.length(); i++) {
            char charNum = s.charAt(i);
            if(charNum == ' ') {
                int intNum = Integer.parseInt(tmpNum.toString());
                minNum = intNum < minNum ? intNum : minNum;
                maxNum = intNum > maxNum ? intNum : maxNum;

                tmpNum = new StringBuilder();
            } else {
                tmpNum.append(charNum);
            }
        }

        int intNum = Integer.parseInt(tmpNum.toString());
        minNum = intNum < minNum ? intNum : minNum;
        maxNum = intNum > maxNum ? intNum : maxNum;

        StringBuilder answer = new StringBuilder();
        answer.append(minNum);
        answer.append(" ");
        answer.append(maxNum);
        return answer.toString();
    }
}
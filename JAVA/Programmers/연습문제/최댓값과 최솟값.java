// 풀이 1
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


class Solution {
    public String solution(String s) {
        String[] tmp = s.split(" ");

   1     int min, max, n;
        min = max = Integer.parseInt(tmp[0]);
        for (int i = 1; i < tmp.length; i++) {
                n = Integer.parseInt(tmp[i]);
            if(min > n) min = n;
            if(max < n) max = n;
        }

        return min + " " + max;
    }
}
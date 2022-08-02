class Solution {
    public int[] solution(int[] answers) {
        int[] a = new int[]{1, 2, 3, 4, 5};
        int[] b = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] c = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int[] score = new int[3];
        for(int i=0; i<answers.length; i++){
            if (answers[i] == a[i%5]) score[0]++;
            if (answers[i] == b[i%8]) score[1]++;
            if (answers[i] == c[i%10]) score[2]++;
        }
        
        int maxCorrect = 0;
        for(int i : score){
            if (maxCorrect < i) maxCorrect = i;
        }
        
        int maxCount = 0;
        for(int i : score){
            if (i == maxCorrect) maxCount++;
        }
        
        int answer[] = new int[maxCount];
        int idx = 0;
        for(int i=0; i<3; i++){
            if (score[i] == maxCorrect) {
                answer[idx] = i+1;
                idx++;
            }
        }
        
        return answer;
    }
}
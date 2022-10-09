import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> notContinuous = new ArrayList<>();

        int beforeN = -1;
        for (int n : arr) {
            if (beforeN != n) {
                notContinuous.add(n);
                beforeN = n;
            }
        }

        int[] answer = new int[notContinuous.size()];

        for (int i = 0; i < notContinuous.size(); i++) {
            answer[i] = notContinuous.get(i);
        }

        // int[] answer = notContinuous.stream().mapToInt(Integer::intValue).toArray();

        return answer;
    }
}
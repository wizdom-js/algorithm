import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> tmp = new ArrayList<>();
        for (int n : arr) {
            if (n % divisor == 0) {
                tmp.add(n);
            }
        }

        if (tmp.size() == 0) {
            tmp.add(-1);
        }

        Collections.sort(tmp);
        int[] answer = tmp.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}

class Solution {
      public int[] solution(int[] arr, int divisor) {
              int[] answer = Arrays.stream(arr).filter(factor -> factor % divisor == 0).toArray();
              if(answer.length == 0) answer = new int[] {-1};
              java.util.Arrays.sort(answer);
              return answer;
      }
}
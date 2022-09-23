import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;

        int[] arr = new int[(int)Math.log10(n)+1];
        int arrL = arr.length;
        for(int i = 0; i < arrL; i++){
            arr[i] = (int)(n % 10);
            n /= 10;
        }

        Arrays.sort(arr);
        for(int i = 0; i < arrL; i++){
            answer += arr[i] * Math.pow(10, i);
        }

        return answer;
    }
}
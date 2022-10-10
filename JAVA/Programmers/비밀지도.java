import java.util.*;
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for (int i = 0; i < n; i++) {
            int[] binary1 = toBinary(n, arr1[i]);
            int[] binary2 = toBinary(n, arr2[i]);

            StringBuilder combineX = new StringBuilder(n);
            for (int j = 0; j < n; j++) {
                if (binary1[j] + binary2[j] > 0) {
                    combineX.append("#");
                } else {
                    combineX.append(" ");
                }
            }

            answer[i] = combineX.toString();
        }
        return answer;
    }

    // 2진수로 변환하기
    public int[] toBinary(int binarySize, int n) {
        int[] binary = new int[binarySize];
        int idx = binarySize - 1;
        while (n > 0) {
            binary[idx] = n % 2;
            n /= 2;
            idx--;
        }

        return binary;
    }
}
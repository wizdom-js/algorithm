import java.util.*;

// 처음 풀이 => 작은 수 구하기는 for문 이용, 작은 수 뺀 배열은 stream 이용
class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) {
            int[] answer = {-1};
            return answer;
        } else {
            int minNumber = 99999999;
            for (int n : arr) {
                minNumber = Math.min(minNumber, n);
            }
            final int lamdaN = minNumber;
            return Arrays.stream(arr).filter(n -> n != lamdaN)
                .toArray();
        }
    }
}


// Stream 사용 -> 속도 문제
class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) {
            return new int[] {-1};
        }

        int minNumber = Arrays.stream(arr).min().getAsInt();
        int[] answer = Arrays.stream(arr).filter(n -> n != minNumber).toArray();
        return answer;
    }
}


// stream 안쓴 for 문으로만 풀이
class Solution {
    public int[] solution(int[] arr) {
        int arrLen = arr.length;
        if (arrLen == 1) {
            return new int[] {-1};
        }

        int minNumber = 99999999;
        for (int n : arr) {
            minNumber = Math.min(minNumber, n);
        }

        int[] answer = new int[arrLen - 1];
        int idx = 0;
        for (int n : arr) {
            if (n != minNumber) {
                answer[idx] = n;
                idx++;
            }
        }
        return answer;
    }
}



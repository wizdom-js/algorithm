class Solution {
   public static int solution(int []A, int []B) {
        int answer = 0;
        min_arr(A);
        max_arr(B);
        for (int i = 0; i < A.length; i++) {
                answer += A[i] * B[i];

        }
        return answer;
   }

   static int[] minSortArr(int[] arr) {
        int minArr = arr[0];
        for (int i = 0; i < arr.length; i++) {
            for (int j = i+1; j < arr.length; j++) {
                if (arr[i] < arr[j]) {
                    minArr = arr[i];
                    arr[i] = arr[j];
                    arr[j] = minArr;
                }
            }
        }
        return arr;
   }

   static int[] maxSortArr(int[] arr) {
        int maxArr = A[0];

        for (int i = 0; i < arr.length;i++) {
            for(int j = i+1; j < arr.length; j++) {
                if(arr[i] > arr[j]) {
                    maxArr = arr[i];
                    arr[i] = arr[j];
                    arr[j] = maxArr;
                }
            }
        }
        return arr;
    }

}
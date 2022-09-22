import java.lang.Math;

class Solution {
    public long solution(long n) {
        long sqrt = (long)Math.sqrt(n);
        if (Math.pow(sqrt, 2) == n){
            return (long)Math.pow(sqrt+1, 2);
        }
        return -1;
    }
}
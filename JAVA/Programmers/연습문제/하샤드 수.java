class Solution {
    public boolean solution(int x) {
        int digitSum = 0;
        int tmpX = x;
        while(tmpX > 0){
            digitSum += tmpX % 10;
            tmpX /= 10;
        }
        return x % digitSum == 0 ? true : false;
    }
}
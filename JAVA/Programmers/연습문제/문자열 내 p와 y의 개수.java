class Solution {
    boolean solution(String s) {
        int pCnt = 0;
        int yCnt = 0;
        for(int i=0; i < s.length(); i++){
            char alphabet = s.charAt(i);
            if(alphabet == 'p' || alphabet == 'P'){
                pCnt++;
            }else if(alphabet == 'y' || alphabet == 'Y'){
                yCnt++;
            }
        }

        return pCnt == yCnt ? true : false;
    }
}

// 개선 풀이
class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        int cnt = 0;
        for(int i=0; i < s.length(); i++){
            char alphabet = s.charAt(i);
            if(alphabet == 'p'){
                cnt++;
            }else if(alphabet == 'y'){
                cnt--;
            }
        }

        return cnt == 0 ? true : false;
    }
}
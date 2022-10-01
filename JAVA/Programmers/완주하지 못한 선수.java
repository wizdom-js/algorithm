import java.util.*;

// 처음 풀었던 내용
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hashMap = new HashMap<String, Integer>(participant.length);
        for (String p : participant) {
            if (hashMap.containsKey(p)) {
                int cnt = hashMap.get(p) + 1;
                hashMap.replace(p, cnt);
            } else {
                hashMap.put(p, 1);
            }
        }

        for (String c : completion) {
            int cnt = hashMap.get(c);
            hashMap.replace(c, cnt - 1);
        }

        for (String p : hashMap.keySet()) {
            int cnt = hashMap.get(p);
            if (cnt > 0) {
                answer = p;
                break;
            }
        }

        return answer;
    }
}

// 개선된 코드
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> hashMap = new HashMap<>(participant.length);
        for (String p : participant) {
            hashMap.put(p, hashMap.getOrDefault(p, 0) + 1);
        }

        for (String c : completion) {
            int cnt = hashMap.get(c);
            hashMap.put(c, cnt - 1);
        }

        for (String p : hashMap.keySet()) {
            int cnt = hashMap.get(p);
            if (cnt > 0) {
                answer = p;
                break;
            }
        }

        return answer;
    }
}
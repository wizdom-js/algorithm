import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> hm = new HashMap<>();
        
        for (String pc : participant){
            hm.put(pc, hm.getOrDefault(pc, 0)+1);
        }
        
        for (String cp : completion){
            hm.put(cp, hm.get(cp)-1);
        }
        
        for (String key : hm.keySet()){
            if (hm.get(key) != 0) {
                answer = key;
                break;
            }
        }
        return answer;
    }
}
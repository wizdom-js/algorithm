import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> bridge = new LinkedList<>();
        int bridge_weight = 0;

        for (int truck : truck_weights) {
            while (true) {
                if (bridge.size() < bridge_length) {
                    if (bridge_weight + truck <= weight) {
                        bridge.offer(truck);
                        bridge_weight += truck;
                        answer++;
                        break;
                    } else {
                        bridge.offer(0);
                        answer++;
                    }
                } else {
                    bridge_weight -= bridge.poll();
                }
            }
        }
        return answer + bridge_length;
    }
}
import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;
        Queue<Integer> bridge = new LinkedList<>();
        int bridge_weight = 0;

        for (int truck : truck_weights) {
            while (true) {
                if (bridge.size() < bridge_length) {    // 다리 꽉 차있지 않은 경우
                    if (bridge_weight + truck <= weight) {  // 무게 때문에 트럭 올라갈 수 있는 경우
                        bridge.offer(truck);
                        bridge_weight += truck;
                        time++;
                        break;
                    } else {    // 트럭 올라가지 못하는 경우
                        bridge.offer(0);
                        time++;
                    }
                } else {
                    bridge_weight -= bridge.poll();
                }
            }
        }
        return time + bridge_length;
    }
}
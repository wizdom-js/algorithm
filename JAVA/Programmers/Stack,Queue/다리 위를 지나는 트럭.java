import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> bridge = new LinkedList<>();
        int bridge_weight = 0;

        // bridge.offer(0);
        // bridge.offer(0);
        int idx = 0;
        while (idx < truck_weights.length) {
            int out_truck = bridge.poll();

            int truck = truck_weights[idx];
            if (bridge_weight + truck <= weight){
                bridge.offer(truck);
                bridge_weight += truck;
            }
            idx++;
        }
        return answer;
    }
}
import heapq


def solution(n, paths, gates, summits):
    def find_intensity():
        dist = [float('inf') for _ in range(n + 1)]

        queue = []
        # 시작점 모두 넣기 => 어디서 시작하든 상관 없으므로
        for gate in gates:
            heapq.heappush(queue, [0, gate])
            dist[gate] = 0

        answer = [0, 9999999999]

        while queue:
            intensity, now = heapq.heappop(queue)

            # 이미 더 가까운 거리가 있다면 패스
            if dist[now] < intensity:
                continue

            # 산봉우리인 경우
            # if now in summits:
            if summits_bit & (1 << now):
                if intensity < answer[1]:
                    answer[0] = now
                    answer[1] = intensity
                elif intensity == answer[1]:
                    answer[0] = min(answer[0], now)
                continue

            # 현재(now) 지점에서 이어진 다음 지점 가보기
            for nxt, nxt_i in point_info[now]:
                # intensity가 가장 최소가 되도록 등산코스를 정해야 함
                # 그리고 현재 등산코스에서 가장 큰 intensity를 찾아야 하니 더 큰 것을 선택
                choosed_i = nxt_i if nxt_i > intensity else intensity
                if choosed_i < dist[nxt]:
                    dist[nxt] = choosed_i
                    heapq.heappush(queue, [choosed_i, nxt])

        # 처음 풀었던 방식 => summit이 숫자 크기대로 주어진게 아니라서 한번 정렬을 해야하고 summit을 한번 더 돌아야하기 때문에 시간초과가 난다.
        # answer = [0, 9999999999]
        # for summit in summits:
        #     if dist[summit] < answer[1]:
        #         answer[0] = summit
        #         answer[1] = dist[summit]
        #
        # return answer

        return answer

    point_info = [[] for _ in range(n + 1)]

    for point1, point2, time in paths:
        point_info[point1].append([point2, time])
        point_info[point2].append([point1, time])

    # 산봉우리 확인하기 위한 비트
    summits_bit = 0
    for i in summits:
        summits_bit |= 1 << i

    return find_intensity()
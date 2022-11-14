import sys
sys.stdin = open('input.txt')

import heapq

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort()

meeting_rooms = [meetings[0][1]]
for meeting in meetings[1:]:
    if meeting_rooms[0] > meeting[0]:
        heapq.heappush(meeting_rooms, meeting[1])
    else:
        heapq.heapreplace(meeting_rooms, meeting[1])

print(len(meeting_rooms))
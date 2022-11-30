import sys
sys.stdin = open('input.txt')

import heapq

problem_n = int(input())
min_heap = []
max_heap = []
for _ in range(problem_n):
    problem_number, problem_level = map(int, input().split())
    heapq.heappush(min_heap, [problem_level, problem_number])
    heapq.heappush(max_heap, [-problem_level, -problem_number])

command_n = int(input())
for _ in range(command_n):
    command = list(input().split())
    if command[0] == "add":
        problem_number, problem_level = int(command[1]), int(command[2])
        heapq.heappush(min_heap, [problem_level, problem_number])
        heapq.heappush(max_heap, [-problem_level, -problem_number])
    elif command[0] == "solved":
        target_problem_number = int(command[1])
        heap_length = len(min_heap)
        min_flag = True
        max_flag = True
        for i in range(heap_length):
            if min_flag and min_heap[i][1] == target_problem_number:
                min_heap = min_heap[:i] + min_heap[i+1:]
                min_flag = False
            if max_flag and max_heap[i][1] == -target_problem_number:
                max_heap = max_heap[:i] + max_heap[i+1:]
                max_flag = False
    elif command[0] == "recommend":
        if command[1] == "1":
            hardest_problem = heapq.heappop(max_heap)
            print(-hardest_problem[1])
            heapq.heappush(max_heap, hardest_problem)
        elif command[1] == "-1":
            easiest_problem = heapq.heappop(min_heap)
            print(easiest_problem[1])
            heapq.heappush(min_heap, easiest_problem)




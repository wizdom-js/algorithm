import sys
sys.stdin = open('input.txt')

import heapq
input = sys.stdin.readline

problem_n = int(input())
min_heap = []
max_heap = []
is_solved = dict()
for _ in range(problem_n):
    problem_number, problem_level = map(int, input().split())
    heapq.heappush(min_heap, (problem_level, problem_number))
    heapq.heappush(max_heap, (-problem_level, -problem_number))
    is_solved[problem_number] = False

command_n = int(input())
for _ in range(command_n):
    command = list(input().split())
    if command[0] == "add":
        problem_number, problem_level = int(command[1]), int(command[2])
        while is_solved[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        while is_solved[min_heap[0][1]]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, (problem_level, problem_number))
        heapq.heappush(max_heap, (-problem_level, -problem_number))
        is_solved[problem_number] = False
    elif command[0] == "solved":
        is_solved[int(command[1])] = True
    elif command[0] == "recommend":
        if command[1] == "1":
            while is_solved[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        elif command[1] == "-1":
            while is_solved[min_heap[0][1]]:
                heapq.heappop(min_heap)
            print(min_heap[0][1])




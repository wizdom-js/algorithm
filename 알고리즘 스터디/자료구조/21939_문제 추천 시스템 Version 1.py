import sys
sys.stdin = open('input.txt')

import heapq

problem_n = int(input())
problem_list = []
for _ in range(problem_n):
    problem_number, problem_level = map(int, input().split())
    heapq.heappush(problem_list, [problem_level, problem_number])

command_n = int(input())
for _ in range(command_n):
    command = list(input().split())
    if command[0] == "add":
        heapq.heappush(problem_list, [int(command[2]), int(command[1])])
    elif command[0] == "solved":
        target_problem_number = int(command[1])
        for i in range(len(problem_list)):
            if problem_list[i][1] == target_problem_number:
                problem_list = problem_list[:i] + problem_list[i+1:]
                break
    elif command[0] == "recommend":
        if command[1] == "1":
            # tmp = heapq.nlargest(len(problem_list), problem_list)[1:]
            # heapq.heapify(tmp)
            # print(tmp, problem_list)
            # print(problem_list[0][1])
            # heapq.heappush(tmp, problem_list[0])
            # problem_list = tmp
            print(heapq.nlargest(1, problem_list)[0][1])
        elif command[1] == "-1":
            print(heapq.nsmallest(1, problem_list)[0][1])



import sys
sys.stdin = open('input.txt')

def devideSection(x, y, d1, d2):
    global area, population
    area = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, d1+1):
        print(x, y, d1, d2, i)
        area[x+i][y-i] = 5
        area[x+d2+i][y+d2-i] = 5

    for i in range(1, d2+1):
        area[x+i][y-i] = 5
        area[x+d1+i][y+d1-i] = 5

    population = [0, 0, 0, 0, 0]
    inputSection(1, x+d1, 1, y+1, 0)
    inputSection(1, x+d2+1, y+1, n+1, 1)
    inputSection(x+d1, n+1, 1, y-d1+d2, 2)
    inputSection(x+d2+1, n+1, y-d1+d2, n+1, 3)

    total_population = sum(sum(jaehyunsi[i]) for _ in range(n))
    population[4] = total_population - sum(population[:4])

    return max(population) - min(population)



def inputSection(x_s, x_e, y_s, y_e, section):
    for x in range(x_s, x_e):
        for y in range(y_s, y_e):
            if area[x][y] == 5:
                break
            population[section] += jaehyunsi[x][y]


n = int(input())
jaehyunsi = [[] for _ in range(n+1)]
for i in range(1, n+1):
    jaehyunsi[i] = [0] + list(map(int, input().split()))

answer = 999999999999999
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if x + d1 + d2 > n:
                    continue
                if y - d1 < 1 or y + d2 > n:
                    continue
                tmp = devideSection(x, y, d1, d2)
                if tmp < answer:
                    answer = tmp

print(answer)
import sys
sys.stdin = open('input.txt')

from collections import deque


# 글자 하나씩 보기
def bfs():
    visited = [0 for _ in range(n + 1)]
    queue = deque([[[1], 1]])   # [[알파벳], 문자열 길이]
    answer = alphabet[1]
    answer_l = 1
    visited[1] = True
    tmp = 'a'   # 붙일 단어를 저장할 변수
    while queue:
        now_apb, l = queue.popleft()

        # 트리 한단계 아래로 내려간 경우 => 다음 알파벳 정해진 경우
        if answer_l != l:
            answer += tmp
            answer_l += 1
            tmp = 'a'


        candi_apb = []  # 다음 가볼 알파벳을 저장할 리스트
        for apb in now_apb: # 현재 알파벳 리스트에서 하나씩 탐색
            for nxt_apb in linked[apb]: # 꺼낸 알파벳에서 연결된 곳 내려가보기
                if not visited[nxt_apb]:
                    visited[nxt_apb] = True
                    if alphabet[nxt_apb] > tmp: # 사전상 뒤에 오는 단어인 경우
                        candi_apb = [nxt_apb]   # 다음 가볼 알파벳 리스트 교체
                        tmp = alphabet[nxt_apb] # 임시 저장하는 알파벳 교체
                    elif alphabet[nxt_apb] == tmp:  # 저장된 단어와 같은 단어인 경우
                        candi_apb.append(nxt_apb)   # 거기도 가보기

        # 다음 가볼 곳이 있다면 큐에 추가 
        if candi_apb:
            queue.append([candi_apb, l + 1])


    return answer


input = sys.stdin.readline
n = int(input())
alphabet = ' ' + input()
linked = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    linked[x].append(y)
    linked[y].append(x)


print(bfs())


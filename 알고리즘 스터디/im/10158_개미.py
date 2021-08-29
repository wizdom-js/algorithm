import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
sx, sy = map(int, input().split())
t = int(input())


re = t // (w-sx+h-sy)
re_re = t % (w-sx+h-sy)




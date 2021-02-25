#문제
#https://www.acmicpc.net/problem/17141
#연구실 2

from itertools import combinations
from collections import deque

def bfs(board,start_loc,N): 
    '''
    ex. 
    시작점이 3개면 전체 시작점 후보(board 중 2인 부분) 중에서 3개를 뽑고
    
    3개 시작점으로 각각 board를 bfs하여 각 matrix의 최대 시간 중(3개) 최솟값을 고름

    골라진 최솟값들 중에서 또 최소가 최소시간
    '''
    chk = [[-1 for i in range(N)] for j in range(N)]
    q = deque()
    q.append(start_loc) 
    chk[start_loc[0]][start_loc[1]] = 0 

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1] 

    while q: 
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N: continue  
            if ny < 0 or ny >= N: continue  
            if board[nx][ny] == '1': continue 
            if chk[nx][ny] != -1: continue  

            chk[nx][ny] = chk[x][y] + 1
            q.append([nx, ny])

    return chk

#-------------------------------------------

N,M = map(int,input().split())
board = [input().split() for j in range(N)]
res = []

loc_list=[(i,j) for i in range(N) for j in range(N) if board[i][j] == '2']
loc_list = list(combinations(loc_list,M)) #중복되지 않은 M개의 좌표 뽑기~

for i in loc_list:
    temp = []
    for j in i:
        temp.append(max(map(max, bfs(board,list(j),N))))
        res.append(min(temp))

print(min(res))
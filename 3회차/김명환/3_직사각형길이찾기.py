import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for i in range(T):
   
    num_list = list(map(int,input().split()))
    num_list.sort()  # 정렬 - 오름차순 ex) xxy or xyy 오름차순으로.
    if num_list[0] != num_list[1]: 
        print(f'#{i+1} {num_list[0]}')# xyy 오름차순으로
    else:
        print(f'#{i+1} {num_list[2]}')# xxy 오름차순으로 -> 정사각형으 경우는 오름차순으로 정렬해도 모든변이 같기때문에 상관없음.
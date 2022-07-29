import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for i in range(T):
    n = int(input())
    num_list = list(map(int,input().split())) 
    avg = sum(num_list)//len(num_list) # 평균 저장하는변수 -> 입력값의 합에서 리스트의 길이 나누어줌. (나머지 제외하고 몫을 저장)
    cnt = 0 # 평균보다 이하인 사람들 카운트
    for j in num_list:
        if j <= avg:
            cnt += 1
    print(f'#{i+1} {cnt}')
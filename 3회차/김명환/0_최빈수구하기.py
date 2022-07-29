# 최빈수 구하기
import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input()) #TC개수
for i in range(T):
    n = int(input()) #TC 순서 
    num_list = list(map(int,input().split())) # 주어진 TC 입력값
    data = {} # TC 별 입력값과 그에 해당하는 최빈수 저장 위한 딕셔너리 
    for j in num_list:
        if j not in data: # 해당 숫자가 딕셔너리에 키 값으로 없으면 추가하고 value 1로 초기화
            data[j] = 1
        else :            # 존재하면 value 에 1추가 
            data[j] +=1 
        max_key = max(data, key=data.get) # value의 최대값에 따라 키 구하는 get함수 사용.
    print(f'#{i+1} {max_key} ')
        

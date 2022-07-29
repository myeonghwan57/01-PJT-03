import sys

sys.stdin = open("_신용카드만들기1.txt")
# 1. 홀수자리마다 x2 해서 더한다 
# 2. 짝수자리는 그대로 더한다.
# 1+2 한 값을 N을 더한 수가 10의 배수이면 유효한 숫자.
T = int(input())
for i in range(T):
    num_list = list(map(int,input().split()))
    result =0
    for j in range(len(num_list)):
        if (j+1) % 2 == 1:
            num_list[j] = (num_list[j])*2
    sum_= sum(num_list)        
    if sum_ % 10 == 0:  
        result = 0
    else:
        result = 10 - (sum_ % 10) # 
    print(f'#{i+1} {result}')
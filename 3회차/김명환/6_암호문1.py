import sys

sys.stdin = open("_암호문1.txt")
# 0 ~ 999999 사이의 수를 나열하여 만든 암호문
# 1. I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]
T = 10 
for k in range(1, 11):
    n = int(input()) # 원본 암호문의 길이 
    num_list = list(map(int, input().split())) # 원본 암호문 
    m = int(input()) # 명령어 개수
    order = list(input().split()) #명령어

    for i in range(len(order)):
        pos = 0 # 명령어가 들어 가야할 포지션
        o_list = [] #명령어 에서 삽입해줘야 하는 숫자들만 따로 리스트 생성 
        if order[i] == 'I': #총 명령어 리스트에서 insert 명령어 일때 
            o_list = order[i+3:i+3+int(order[i+2])] # 명령어가 들어가야 하는 개수 즉, I, x, y, s 에서 y를 사용해 삽입해야 하는 명령어만 추출
            pos = int(order[i+1]) # 원래 암호문에서 들어가야하는 위치 
            for j in range(len(o_list)): # 삽입 
                num_list.insert(pos+j,int(o_list[j]))
            

    print('#%d' % k, end=' ')
    print(*num_list[:10])
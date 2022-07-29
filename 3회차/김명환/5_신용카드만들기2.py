import sys

sys.stdin = open("_신용카드만들기2.txt")
# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.
# EX) 6471-6836-9525-5276
# EX) 3029192045012901

T = int(input())
start_num = ['3','4','5','6','9']
for i in range(T): 
    n = input()
    card_num = n.replace('-','')
    result = 0
    if len(card_num) != 16:
        result = 0
    elif card_num[0] not in start_num:
        result = 0
    else:
        result = 1
    print(f'#{i+1} {result}')
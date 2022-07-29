import sys

sys.stdin = open("_문자열의거울상.txt")

#b <-> d
#p <-> q
# 순서도 바꿔야 함 -> 거울 
T = int(input())
for i in range(T):
    word = input()
    rev_word = word[::-1] # 문자열 역순 저장
    result = '' # 역순 저장후 거울로 뒤집어야 하는 알파벳 저장하기 위한 변수 선언.
    for j in range(len(rev_word)):
        if rev_word[j] == 'b':
            result += 'd'
        elif rev_word[j] == 'd':
            result += 'b'
        elif rev_word[j] == 'q':
            result += 'p'    
        else:
            result += 'q' 
    print(f'#{i+1} {result}')
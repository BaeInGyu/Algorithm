# sum of between two num.py (the sum of integers between two numbers) 
# Date of creation: 2019-12-21
# Author: Bae InGyu
# 알고리즘 출처: 프로그래머스(https://programmers.co.kr/)
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
# 제한 조건
# a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
# a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.
# 입출력 예
# a	 b	return
# 3	 5	12
# 3	 3	3
# 5	 3	12


def solution(a,b):
    answer = 0
    #If B is greater than A
    if a <b:
        #Initialize integer values from a to b on i
        for i in range(a,b+1):
            #Initializing the sum of i in the answer
            answer += i
    #If A and B are the same number,
    elif a == b:
        #Initialize the value of a in the answer
        answer = a
    #If A is greater than B
    else:
        #Initialize integer values from a to b on i
        for i in range(a,b-1,-1):
            ##Initializing the sum of i in the answer
            answer +=i
    #Returns an answer
    return answer

solution(3,5)
    
    

# equal of counting.py 
# Date of creation: 2019-12-17
# Author: Bae InGyu
# 알고리즘 출처: 프로그래머스(https://programmers.co.kr/)
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True 다르면 False를 return 하는 solution를 완성하세요. 
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
# 입출력 예
# s		answer
# pPoooyY	true
# Pyy		false
# 입출력 예 설명
# 입출력 예 #1
# 'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.
# 입출력 예 #2
# 'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.


def solution(s):
    #Convert all strings to lowercase
    lower = s.lower()
    #If the number of y characters and the number of p characters are the same return true
    if lower.count('y') == lower.count('p'):
                   return True
    #If 0 is obtained by adding y and p characters return true
    elif (lower.count('y')+lower.count('p')) == 0:
                   return True
    #Else return false
    else:
                   return False

s = 'pPoooyY' 
solution(s)

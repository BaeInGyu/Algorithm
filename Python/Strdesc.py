# Strdesc.py 
# Date of creation: 2019-12-16
# Author: Bae InGyu
# 알고리즘 출처: 프로그래머스(https://programmers.co.kr/)
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
#  s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
# 입출력 예
# s	       return
# 'Zbcdefg'     'gfedcbZ'



def solution(s):
    #Convert String to Array
    answer = list(s)
    #Arrange elements in an array in descending order
    answer.sort(reverse=True)
    #Convert Array to String and return
    answer = ('').join(answer)
    return answer

s = 'Zbcdefg'
solution(s)
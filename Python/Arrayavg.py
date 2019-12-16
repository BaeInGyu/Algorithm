# Arrayavg.py 
# Date of creation: 2019-12-16
# Author: Bae InGyu
# 알고리즘 출처: 프로그래머스(https://programmers.co.kr/)
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
# 입출력 예
# arr	     return
# [1,2,3,4]     2.5
# [5,5]          5


def solution(arr):
	#Declaring and initializing variables to store results
	answer = 0
	#The index of the array is i and the elements are j
	for i,j in enumerate(arr):
		#The total sum of the array elements is obtained.
		answer += arr[i]
	#Divide the sum by the number of elements in the array and return
	answer = answer/(i+1)        
	return answer

arr = [1,2,3,4]
solution(arr)

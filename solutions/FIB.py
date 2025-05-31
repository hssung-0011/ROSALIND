"""Rabbits and Recurrence Relations"""


'''
n과 k가 주어진다.
토끼가 성장하는데 2개월이 걸리고, 그 이후엔 매달 k쌍의 토끼를 낳는다.
이 때 n개월 후 토끼는 몇 쌍이 되는가?
'''


input_file = open('/mnt/c/Users/jsml6/Downloads/rosalind_fib.txt', 'r').read().rstrip().split()
input_number = int(input_file[0]), int(input_file[1]) # n, k


def next_month(num1, num2 ,k):
    """ 한 쌍의 토끼가 k쌍의 토끼를 낳고, 지난달 토끼수가 num1, 이번달의 토끼 수가 num2일 때 다음달의 토끼 수"""
    return num1 * k + num2

rabbit_num = [1, 1]

while len(rabbit_num) < input_number[0]:
    rabbit_num.append(next_month(rabbit_num[-2], rabbit_num[-1], input_number[1]))
    continue

# print(rabbit_num)
print(rabbit_num[-1])
    

 

"""
피보나치 수열(Fibonacci Sequence)을 계산하는 프로그램도 파이썬으로 간단히 작성할 수
있다.

피보나치 수열은 0 과 1 로 시작하고 다음의 숫자는 이전 숫자 두개를 더한 숫자들로
이루어 진다.
0, 1, 1, 2, 3, 5, 8, 13 ......

n 개의 숫자로 이루어진 피보나치 수열을 출력하는 함수를 작성하라.
"""
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    old, new = 0, 1
    for _ in range(n):
        #         tmp = old + new
        #         old = new
        #         new = tmp
        old, new = new, old + new
    return old

lst = []
for i in range(10):
    lst.append(fib(i))

print(lst)
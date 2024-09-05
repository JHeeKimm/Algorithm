# n이 주어졌을 때, 재귀호출 코드와 동적 프로그래밍 코드의 각 실행 횟수를 한 줄에 출력하기!

# 입력 받기
n = int(input())

def recursive_fib(n):
    if n == 1 or n == 2: # 기저 조건 : n이 1 또는 2일 때, 피보나치 값 1 반환
        return 1
    else:
        return (recursive_fib(n - 1) + recursive_fib(n - 2))


def dp_fib(n):
    # f[0]은 사용되지 않고, 인덱스 1부터 n개까지 사용하기 위해 n+1로 함
    f = [0]*(n+1)

    f[1], f[2] = 1, 1
    count_dp = 0

    for i in range(3, n+1): # 3부터 n까지 반복
        f[i] = f[i-1] + f[i-2]
        count_dp += 1
    return count_dp


print(recursive_fib(n), dp_fib(n))
import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))

def solution(numbers):
    x = 1
    while True:
        count = 0
        for num in numbers:
            if x % num == 0:
                count += 1
        if count >= 3:
            return x
        x += 1

print(solution(numbers))
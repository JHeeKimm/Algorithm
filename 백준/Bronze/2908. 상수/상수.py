# 두 수가 주어지면, 그 수를 거꾸로 만들고 그 중 큰 수를 출력한다.
a, b = input().split()

reversed_a = int(''.join(reversed(a)))
reversed_b = int(''.join(reversed(b)))

print(max(reversed_a, reversed_b))
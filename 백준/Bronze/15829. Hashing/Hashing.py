l = int(input())
s = list(input())

result = 0

for i in range(l):
    result += (ord(s[i])-96) * (31**i)

print(result % 1234567891)
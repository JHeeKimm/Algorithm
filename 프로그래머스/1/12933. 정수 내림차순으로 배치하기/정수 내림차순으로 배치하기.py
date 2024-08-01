def solution(n):
    str_n = str(n)
    sorted_str_n = sorted(str_n, reverse=True)
    sorted_n = int(''.join(sorted_str_n))
    return sorted_n
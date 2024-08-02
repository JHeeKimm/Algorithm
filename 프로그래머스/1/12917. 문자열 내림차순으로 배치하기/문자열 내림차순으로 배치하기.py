def solution(s):
    sorted_str = sorted(s, reverse=True)
    lower = ''
    upper = ''
    for char in sorted_str:
        if char.islower():
            lower += char
        else: upper += char
    return lower + upper
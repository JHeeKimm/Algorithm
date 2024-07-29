def solution(s):
    if s[:1] == ')' or s[-1:] == '(':
        return False
    
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
        
    return count == 0
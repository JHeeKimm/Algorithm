def solution(str):
    result = 0
    size=len(str)
    temp = 0
    if str [0] == '-' :
        sign = -1
    else :
        sign = 1
    for i in range(0, size) :
        if str[i] == '1' :
            temp = 1
        elif str[i] == '2' :
            temp = 2
        elif str[i] == '3' :
            temp = 3
        elif str[i] == '4' :
            temp = 4
        elif str[i] == '5' :
            temp = 5
        elif str[i] == '6' :
            temp = 6
        elif str[i] == '7' :
            temp = 7
        elif str[i] == '8' :
            temp = 8
        elif str[i] == '9' :
            temp = 9
        else :
            temp = 0
        for i in range(size-i-1) :
            temp = temp * 10
        result = result + temp
    result = result * sign
    return result
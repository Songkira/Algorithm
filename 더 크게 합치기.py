def solution(a, b):
# 풀이 1---------------
    return int(max(f'{a}{b}', f'{b}{a}'))
# 풀이 1---------------
    a, b = str(a), str(b)
    return int(max(a+b, b+a))
# 내 풀이 --------
    # answer = 0
    # plus_number1 = str(a) + str(b)
    # plus_number2 = str(b) + str(a)
    # int_plus1 = int(plus_number1)
    # int_plus2 = int(plus_number2)
    # if int_plus1 < int_plus2:
    #     return int_plus2
    # elif int_plus1 > int_plus2:
    #     return int_plus1
    # else:
    #     return int_plus1
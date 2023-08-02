def solution(ineq, eq, n, m):
## 내 풀이--------------------------------
    # if ineq == '>':
    #     if eq == '=':
    #         if n >= m:
    #             return 1
    #         else:
    #             return 0
    #     else:
    #         if n > m:
    #             return 1
    #         else:
    #             return 0
    # else:
    #     if eq == '=':
    #         if n <= m:
    #             return 1
    #         else:
    #             return 0
    #     else:
    #         if n < m:
    #             return 1
    #         else:
    #             return 0
## 풀이1
    # return int(eval(str(n) + ineq + eq.replace('!', '') + str(m)))\
## 풀이2
    # if eq == '!':
    #     eq = ''
    # return int(eval(f'{n} {ineq}{eq} {m}'))
## 풀이3
    answer = 0
    if n > m and ineq == ">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1

    return answer
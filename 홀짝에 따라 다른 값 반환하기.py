def solution(n):
## 내풀이 ------------------------
#     odd_n = 1
#     even_n = 0
#     basic = 0
#     if n % 2 :
#         for _ in range((n//2) + 1):
#             basic += odd_n
#             odd_n += 2
#     elif n % 2 != 1 :
#         for _ in range((n//2) + 1):
#             # basic += even_n ** even_n
#             basic += pow(even_n, 2)
#             even_n += 2
#     # answer = 0
#     return basic
## 풀이1
    # if n%2:
    #     return sum(range(1,n+1,2))
    # return sum([i*i for i in range(2,n+1,2)])
## 풀이2
    # answer = 0
    # if n % 2:
    #     for i in range(1, n + 1, 2):
    #         answer += i
    # else:
    #     for i in range(2, n + 1, 2):
    #         answer += i ** 2
    # return answer
## 풀이3
    answer = 0
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            answer += i ** 2
    else:
        for i in range(1, n + 1, 2):
            answer += i

    return answer


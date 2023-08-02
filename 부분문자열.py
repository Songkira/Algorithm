def solution(str1, str2):
    M = len(str1) # 부분문자열
    N = len(str2) # 전체문자열
    i = 0   # str2의 인덱스
    j = 0   # str1의 인덱스
    while j < M and i < N :
        if str2[i] != str1[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return 1
    else : return 0
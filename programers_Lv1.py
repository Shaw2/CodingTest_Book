n = 8
m = 4
section = [2, 3, 8]

def solution(n, m, section):
    answer = 0

    b = len(section)
    a = b-1
    while True:
        if section[b] - section[a] >= m:
            answer = answer + 1
        b = b - 1
        a = a - 1
        if a == 0:
            break

    b = len(section)
    a = b - 1
    while True:
        if section[b] - section[a] == m-1:
            answer = answer + 1
        a = a - 1
        if b - a == m-1:



    return answer
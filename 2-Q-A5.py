def solution(n, s):
    if s < 2:
        return [-1]
    return [s//2, s-s//2]

n = 2
s = 9834567
answer = solution(n, s)
print(answer)
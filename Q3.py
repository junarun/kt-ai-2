#Q3
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if (i**(1/2)).is_integer():
            answer -= i
        else:
            answer += i
    return answer

left, right = map(int, input().split())
c = solution(left, right)
print(c)
print(c)
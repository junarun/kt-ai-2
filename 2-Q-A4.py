#2-Q-A4
def solution(arr):
    min_val = min(arr)
    max_val = max(arr)
    count = 0
    while 1:
        for a in arr:
            if max_val % a == 0:
                count += 1
        if count == len(arr): break
        else: count = 0
        max_val += min_val
    return max_val

arr = [1,2,3,4,5,6,7,8,9,10]
answer = solution(arr)
print(answer)
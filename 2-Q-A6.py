def solution(arr):
    min_val = min(arr)
    while min_val in arr:
        arr.remove(min_val)
    return arr if arr else [-1]

arr = [10,1]
answer = solution(arr)
print(answer)
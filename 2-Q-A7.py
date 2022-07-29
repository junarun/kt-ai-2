def solution(arr):
    before = arr[0]
    answer = []
    for i in range(1,len(arr)):
        now = arr[i]
        if before == now:
            continue
        else:
            answer.append(before)
            before = now
    answer.append(arr[-1])
    return answer

arr = [1,1,3,3,0,1,1]
arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)
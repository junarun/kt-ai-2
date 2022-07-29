def solution(lottos, win_nums):
    answer = []
    win_nums.append(0)
    grade = 7
    zero = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            grade -= 1
    if grade == 7: grade = 6
    if zero == 6: zero = 5
    answer.append(grade)
    answer.append(grade+zero)
        
    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [45, 4, 35, 20, 3, 9]

print(solution(lottos, win_nums))
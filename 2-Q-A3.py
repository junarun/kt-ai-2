#2-Q-A3
def solution(store, customer):
    answer = ['yes', 'no']
    result = []
    for product in customer:
        if product in store:
            result.append(answer[0])
        else:
            result.append(answer[1])
    return result

store = [2,3,7,8,9]
customer = [7,5,9]
answer = solution(store, customer)
print(answer)
#2-Q-A0
N, X = map(int, input().split())  # N, X 를 입력받음
datas = list(map(int, input().split())) # 리스트를 입력받음
answer = []
for data in datas:
    if data < X:
        answer.append(data)

for ans in answer:
    print(ans, end=' ')
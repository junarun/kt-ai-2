#Q4
data = input('숫자로 이루어진 문자열을 입력하세요. ')
cnt = 0
for i in data:
    if i == '0':
        cnt += 1
    else: break

data = data[cnt:]
result = int(data[0])
for i in data[1:]:
    if i == '0':
        result += int(i)
    else:
        result *= int(i)

print(result)
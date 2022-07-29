#2-Q2
array = list(map(int, input().split()))
length = len(array)

for i in range(length//2):
    array[i], array[length - i - 1] = array[length - i - 1], array[i]

for j in array:
    print(j, end=' ') 
#2-Q1 에라토스테네스의 체
n = 1000
a = [False,False] + [True] * (n-1)
prime_number = []
for i in range(2, n+1):
    if a[i]:
        prime_number.append(i)
        for j in range(i*2, n+1, i):
            a[j] = False

print(prime_number)
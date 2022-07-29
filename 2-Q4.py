#2-Q4
a = list(map(int, input().split()))
maximum = a[0]
for i, val in enumerate(a):
    if val > maximum:
        maximum = val
        idx = i
print(f"max(a) = {maximum} index = {idx}")
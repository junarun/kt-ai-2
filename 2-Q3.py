#2-Q3
a = list(map(int, input().split()))
key = int(input())

def bin_search(a, key):
    start = 0
    end = len(a)
    while 1:
        mid = (start + end)//2
        if a[mid] == key:
            return mid
        else:
            if a[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        if start > end: break
    return -1

print(bin_search(a, key))
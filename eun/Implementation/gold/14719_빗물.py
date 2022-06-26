n, m = map(int, input().split())
table = list(map(int, input().split()))

left, right = 0, m-1
max_left, max_right = table[left], table[right]
res = 0
while left < right:
    max_left = max(max_left, table[left])
    max_right = max(max_right, table[right])

    if max_left <= max_right:
        res += max_left-table[left]
        left += 1
    else:
        res += max_right-table[right]
        right -= 1
print(res)

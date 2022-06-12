from bisect import bisect_left, bisect_right


def lowerbound(array, target):
    start, end = 0, len(array)
    while start < end:
        mid = (start+end)//2
        if array[mid] < target:
            start = mid+1
        else:  # lowerbound 이므로 같으면 줄임.
            end = mid
    return end


def upperbound(array, target):
    start, end = 0, len(array)
    while start < end:
        mid = (start+end)//2
        if array[mid] <= target:  # upperbound 이므로 같으면 늘림
            start = mid+1
        else:
            end = mid
    return end


print("start")
print(lowerbound([1, 3, 10, 20, 30], 1))
print(upperbound([1, 3, 10, 20, 30], 1))
print(bisect_left([1, 3, 10, 20, 30], 1))
print(bisect_right([1, 3, 10, 20, 30], 1))
print("----")
print(lowerbound([1, 3, 10, 20, 30], 10))
print(upperbound([1, 3, 10, 20, 30], 10))
print(bisect_left([1, 3, 10, 20, 30], 10))
print(bisect_right([1, 3, 10, 20, 30], 10))
print("----")
print(lowerbound([1, 3, 10, 20, 30], 60))
print(upperbound([1, 3, 10, 20, 30], 60))
print(bisect_left([1, 3, 10, 20, 30], 60))
print(bisect_right([1, 3, 10, 20, 30], 60))
print("----")
print(lowerbound([1, 3, 10, 20, 30], 20))
print(upperbound([1, 3, 10, 20, 30], 20))
print(bisect_left([1, 3, 10, 20, 30], 20))
print(bisect_right([1, 3, 10, 20, 30], 20))
print("----")
print(lowerbound([1, 3, 10, 20, 30], 30))
print(upperbound([1, 3, 10, 20, 30], 30))
print(bisect_left([1, 3, 10, 20, 30], 30))
print(bisect_right([1, 3, 10, 20, 30], 30))
print("----")
print(lowerbound([1, 3, 10, 20, 30], 3))
print(upperbound([1, 3, 10, 20, 30], 3))
print(bisect_left([1, 3, 10, 20, 30], 3))
print(bisect_right([1, 3, 10, 20, 30], 3))
print("----")
print(lowerbound([1, 3, 10, 20, 30], 2))
print(upperbound([1, 3, 10, 20, 30], 2))
print(bisect_left([1, 3, 10, 20, 30], 2))
print(bisect_right([1, 3, 10, 20, 30], 2))
print("----")
print(lowerbound([1, 3, 10, 20, 30], 15))
print(upperbound([1, 3, 10, 20, 30], 15))
print(bisect_left([1, 3, 10, 20, 30], 15))
print(bisect_right([1, 3, 10, 20, 30], 15))
print("----")
print(lowerbound([1, 3, 10, 20, 30], 4))
print(upperbound([1, 3, 10, 20, 30], 4))
print(bisect_left([1, 3, 10, 20, 30], 4))
print(bisect_right([1, 3, 10, 20, 30], 4))
print("----")
print(lowerbound([1, 3, 10, 20, 30], 8))
print(upperbound([1, 3, 10, 20, 30], 8))
print(bisect_left([1, 3, 10, 20, 30], 8))
print(bisect_right([1, 3, 10, 20, 30], 8))
print("----")

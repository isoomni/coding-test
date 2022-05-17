def a(n):
    print("***"*n, end="")


def b(n):
    print("* *"*n, end="")


def solution(n):
    if n < 0:
        return

    if n % 2 == 1:
        a(n)
        print("   "*(n), end="")
        a(n)
        print()
        b(n)
        print("   "*(n), end="")
        b(n)
        print()
        a(n)
        print("   "*(n), end="")
        a(n)
        print()
    else:
        a(n)
        print()
        b(n)
        print()
        a(n)
        print()
        solution(n-1)
        a(n)
        print()
        b(n)
        print()
        a(n)
        print()


n = int(input())
solution(n)

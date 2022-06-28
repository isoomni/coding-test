import sys
input = sys.stdin.readline

def dfs(s: str, t: str) -> int:
    if len(s) == len(t):
        return [0, 1][s == t]

    if t[-1] == 'B':
        if t[0] != 'B':
            return 0
        return dfs(s, t[:0:-1])

    else:
        if t[0] == 'A':
            return dfs(s, t[:-1])
        else:
            return dfs(s, t[:0:-1]) or dfs(s, t[:-1])


def main():
    S = input()
    T = input()
    print(dfs(S, T))
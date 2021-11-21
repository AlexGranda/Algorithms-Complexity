def memoized_trend(j):
    if M[j] is None:
        for k in range(j, n):
            if P[j] < P[k]:
                M[j] = 1 + memoized_trend(k)
                return M[j]
            M[j] = memoized_trend(k+1)
        return M[j]
    return M[j]


if __name__ == '__main__':
    P = [2, 1, 3, 5, 5, 6]

    n = len(P)
    M = []

    for i in range(n-1):
        M.append(None)
    M.append(1)

    memoized_trend(0)

    print(f'The max sequence is of {max(M)} days')
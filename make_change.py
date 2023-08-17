def makeChange(n):
    C = [100, 25, 10, 5, 1]
    S = []
    s = 0

    i = 0

    while i < len(C):
        if s + C[i] > n:
            i = i +1
        else:
            s = s + C[i]
            S.append(C[i])
            if s == n:
                break

    if s == n:
        return S
    return "No solution found"

print(makeChange(299))

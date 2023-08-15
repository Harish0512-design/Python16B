def solution(a, b):
    ''' to check whether two arrays are similar, by just swapping for one time'''
    for i in range(len(a)):
        if a[i] != b[i]:
            if a[i] in b:
                idx = b.index(a[i])
                c = b[idx]
                d = b[i]
                b[i] = c
                b[idx] = d
                break

    for i, j in zip(a, b):
        if i != j:
            return False
    else:
        return True


a = [1, 2, 3]
b = [2, 1, 3]
print(solution(a, b))

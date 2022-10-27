
N = int(input())
X = [int(value) for value in input().split()]
M = [[None]*N for _ in range(N)]

def OPT(i,j):
    if i == j:
        return X[i]
    if i > j:
        return 0
    if M[i][j] == None:
        M[i][j] = max(X[i]+(OPT(i+2,j) if X[i+1]>X[j] else OPT(i+1,j-1)), 
                      X[j]+(OPT(i,j-2) if X[j-1]>X[i] else OPT(i+1,j-1)))
    return M[i][j]

print(f"OPT: {OPT(0, N-1)}")
print(f"M: {M}")

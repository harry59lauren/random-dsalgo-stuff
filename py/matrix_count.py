
def appearances_in_matrix(N, k):
    return len([ n for n in range(1, N + 1) if not k % n and k / n <= N ])

print(appearances_in_matrix(6, 12))
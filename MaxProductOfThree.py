# Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

def solution(A):
    A.sort()
    n = len(A)
    max = 0
    if(A[0] > 0 or A[n-1] < 0):
        return (A[n - 1] * A[n - 2] * A[n - 3])
    a = A[n - 1] * A[0] * A[1]
    b = A[n - 1] * A[n - 2] * A[n - 3]
    return a if a > b else b

def main():
    print(solution([-5, 5, -5, 4]))


if __name__ == "__main__": main()
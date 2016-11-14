# Determine whether a triangle can be built from a given set of edges.

def solution(A):
    A.sort()
    n = len(A)
    if n < 3:
        return 0
    for i in range(n-2):
        if A[i]+A[i+1]>A[i+2] and A[i]+A[i+2]>A[i+1] and A[i+1]+A[i+2]>A[i]:
            return 1
    return 0

def main():
    print(solution([5,3,3]))


if __name__ == "__main__": main()
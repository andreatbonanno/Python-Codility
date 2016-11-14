# Compute number of distinct values in an array.

def solution(A):
    n = len(A)
    if n == 0:
        return 0
    A.sort()
    result = 1
    for k in range(1, n):
        if A[k] != A[k - 1]:
            result += 1
    return result


def main():
    print(solution([5,3,3]))


if __name__ == "__main__": main()
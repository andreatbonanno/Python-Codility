# Find the earliest time when a frog can jump to the other side of a river.


def solution(X, A):
    map = dict()
    for i in range(0, len(A)):
        if A[i] not in map:
            map[A[i]] = i

    seconds = -1

    for x in range(1, X + 1):
        if x not in map:
            return -1
        else:
            if seconds < map[x]:
                seconds = map[x]

    return seconds

def main():
    print(solution(5, list([1,3,1,4,2,3,5,1])))


if __name__ == "__main__": main()
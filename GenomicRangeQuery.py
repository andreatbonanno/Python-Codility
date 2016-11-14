# Find the minimal nucleotide from a range of sequence DNA.
# Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively
# The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.
# There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers.
# The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in
# the DNA sequence between positions P[K] and Q[K] (inclusive).

def solution(S, P, Q):
    A = prefix_sums(binary(S,'A'))
    C = prefix_sums(binary(S,'A'))
    G = prefix_sums(binary(S,'A'))

    print(A)

    m = len(P)
    results = []
    for i in range(m):
        results.append(check_impacts(A,C,G,P[i],Q[i]))

    return results


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def binary(S, char):
    A = []
    n = len(S)
    for s in S:
        if s == char:
            A.append(1)
        else:
            A.append(0)
    return A

def check_impacts(A,C,G,p,q):
    if A[q+1] - A[p] > 0:
        return 1
    elif C[q+1] - C[p] > 0:
        return 2
    elif G[q+1] - G[p] > 0:
        return 3
    else:
        return 4



def main():
    print(solution('CAGCCTA',[2,5,0],[4,5,6]))


if __name__ == "__main__": main()
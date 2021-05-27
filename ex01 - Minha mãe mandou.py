import sys
import math
def read_in():
    L = sys.stdin.readlines()
    for i in range(len(L)):
        L[i] = L[i].replace("\n", "")
    return L
def main():
    L = read_in()
    S = 29
    E = int(L[0])
    for i in range(0, E):
        n, k = L[i + 1].split()
        k = int(k)
        n = int(n)
        V = math.ceil((k * S) / n)
        if V == 0:
            V = 1
        A = (k * S) % n
        print(
            V, A + 1, end=""
        )
        print("")
if __name__ == "__main__":
    main()

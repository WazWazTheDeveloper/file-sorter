from cmath import inf
import sys
def recurseInfinitely( n ):
    i = 1
    recurseInfinitely(n+1)



if __name__ == "__main__":
    sys.setrecursionlimit(2147483647)
    recurseInfinitely(0)
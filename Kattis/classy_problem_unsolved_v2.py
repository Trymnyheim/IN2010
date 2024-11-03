# https://open.kattis.com/problems/classy

from sys import stdin
from heapq import heappush, heappop

def main():
    # Gets input and arranges it into cases:
    T = int(next(stdin)) # Number of cases
    cases = []
    for _ in range(T):
        n = int(next(stdin)) # Number of objects in case
        names = dict()
        for _ in range(n):
            object, classes = next(stdin).strip().split(": ")
            classes, _ = classes.split() # Get rid of the " class"
            classes = classes.split("-")
            rank = 0
            for i in range(10):
                if i < len(classes):
                    if classes[i] == "upper":
                        rank += 2
                    elif classes[i] == "lower":
                        rank += 0
                    else:
                        rank += 1
                else:
                    rank += 1
            names[object] = rank
        cases.append(names)

    # Iterate over all cases
    for names in cases:
        # Heap sort names:
        sorted = []
        heap = []
        for name in names:
            rank = names[name]
            heappush(heap, (-rank, name))
        while heap:
            rank, name = heappop(heap)
            sorted.append(name)
        # Print output
        for name in sorted:
            print(name)
        print("="*30)   

if __name__ == "__main__":
    main()

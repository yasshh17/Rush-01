import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if x == 1 or y == 1:
        for _ in range(y):
            print("B" * x)
        return

    edge = "A" + "B" * (x - 2) + "C"
    print(edge)
    for _ in range(y - 2):
        print("B" + " " * (x - 2) + "B")
    print(edge)
import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if x == 1 or y == 1:
        for _ in range(y):
            print("*" * x)
        return

    print("/" + "*" * (x - 2) + "\\")
    for _ in range(y - 2):
        print("*" + " " * (x - 2) + "*")
    print("\\" + "*" * (x - 2) + "/")
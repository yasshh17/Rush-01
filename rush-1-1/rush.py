import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if x == 1:
        top = "o"
        middle = "|"
        bottom = "o"
    else:
        top = "o" + "-" * (x - 2) + "o"
        middle = "|" + " " * (x - 2) + "|"
        bottom = "o" + "-" * (x - 2) + "o"

    if y == 1:
        print(top)
        return

    print(top)
    for _ in range(y - 2):
        print(middle)
    print(bottom)
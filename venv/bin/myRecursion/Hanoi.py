def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving from {} to {}".format(a, c))
        hanoi(n-1, b, a, c)

if __name__ == "__main__":
    hanoi(2, 'A', 'B', 'C')

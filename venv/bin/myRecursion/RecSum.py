def recSum(alist):
    if alist:
        return alist.pop() + recSum(alist)
    return 0


if __name__ == "__main__":
    alist = [1, 2, 3, 4, 5]
    print(recSum(alist))
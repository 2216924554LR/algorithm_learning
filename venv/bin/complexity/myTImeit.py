from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l.append(i)

def test2():
    l = []
    for i in range(1000):
        l = l + [i]

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


timer1 = Timer("test1()", "from __main__ import test1")
print(timer1.timeit(1000))

timer2 = Timer("test2()", "from __main__ import test2")
print(timer1.timeit(1000))

timer3 = Timer("test3()", "from __main__ import test3")
print(timer1.timeit(1000))

timer4 = Timer("test4()", "from __main__ import test4")
print(timer1.timeit(1000))


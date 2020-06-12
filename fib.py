import cProfile

from time import gmtime, strftime


def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib1(n - 1) + fib1(n - 2))


def fib2(n):
    arr = [0, 1]

    for i in range(0, n):
        arr.append(arr[-1] + arr[-2])

    return arr[n]


def fib3(n):
    a = 0
    b = 1

    for i in range(0, n):
        a, b = b, a + b

    return a


def runEm():
    n = int(input('Enter n: '))
    # n = 40
    if n >= 0:
        print(strftime("%H:%M:%S", gmtime()), 'fib1:', fib1(n))
        print(strftime("%H:%M:%S", gmtime()), 'fib2:', fib2(n))
        print(strftime("%H:%M:%S", gmtime()), 'fib3:', fib3(n))
    else:
        print('error: n < 0')


if __name__ == '__main__':
    cProfile.run('runEm()')

def recursive(n):
    return 1 if n <= 1 else recursive(n - 1) + recursive(n - 2)


def loop(n):
    fibo = [1, 1, ]
    for i in range(1, n):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo[-1]

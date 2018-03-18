def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    print("Enter a non-negative integer 'n'")
    print("n is: ")
    n = int(input())
    print("Result:")
    print(fib(n))


main()

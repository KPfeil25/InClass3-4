def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)

if __name__ == "__main__":
    num = input("What sequence value do you want to see?\n")
    res = fibonacci(int(num))
    print(res)
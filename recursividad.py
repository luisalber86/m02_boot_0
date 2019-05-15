def retrocontador(num):
    print("{},".format(num), end ="")
    if num > 0:
        retrocontador(num - 1)

retrocontador(10)

def sumatoriorecur(num):
    if num > 0:
        return num + sumatoriorecur(num-1)
    else:
        return 0
    
print("\n {}".format(sumatoriorecur(3)))


def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1

print(factorial(4))

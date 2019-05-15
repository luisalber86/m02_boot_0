def retrocontador(num):
    print("{},".format(num), end ="")
    if num > 0:
        retrocontador(num - 1)

retrocontador(10)
def tripler(array):
    result = []
    for i in range(len(array)):
        num = array[i]
        multiple = num * 3
        result.append(multiple)
    return print(result)

tripler([1,2,3,4,5])
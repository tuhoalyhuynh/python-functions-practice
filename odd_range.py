def oddRange(end):
    arr = []
    for i in range(end):
        i+=1
        if i % 2:
            arr.append(i)
    return print(arr)

oddRange(12)
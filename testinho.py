def fibonacci(num: int):
    if(num == 1):
        return num
    elif(num == 0):
        return 0
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(10))

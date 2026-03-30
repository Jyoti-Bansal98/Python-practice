try:
    num = int(input())
    result = 10 / num

except ZeroDivisionError:
    print("Zero error")

else:
    print("Result:", result)
    print('No error')
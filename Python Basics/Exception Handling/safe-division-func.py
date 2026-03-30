def safe_division(a,b):

    try:
        return a/b
    except ValueError:
        return 'Invalid input'
    except ZeroDivisionError:
        return 'Cannot be divided by 0'
    
a,b = list(map(int,input().split()))
print(safe_division(a,b))


## multiple exception  (ek saath)
try:
    x = int(input())
    print(10 / x)

except (ValueError, ZeroDivisionError):
    print("Invalid input or zero error")




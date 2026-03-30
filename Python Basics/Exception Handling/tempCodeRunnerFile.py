# even if error occur
try:
    a = int(input())
    if a%2 != 0:
        print('odd')
except:
    print('even error occured')
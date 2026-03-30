'''error ho ya na ho → finally chalega'''

try:
    print("Try block")
except:
    print("Error")
finally:
    print("Always runs")



try:
    num = int(input())
    print(10 / num)

except:
    print("Error")

finally:
    print("Always runs")

## even if error occur
try:
    a = int(input())
    if a%2 != 0:
        print('odd')
except:
    print('even error occured')


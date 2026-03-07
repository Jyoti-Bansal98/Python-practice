import time
a = input("enter your name:")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
H = int(time.strftime('%H'))
print(H)

if (H>4 and H<12):
    print("Good morning", a)
    print("have a good day")
elif(H>=12 and H<16):
    print("Good afternoon", a)
    print("finish ur work")
    if(H==14):
        print("lunch time")
    elif(H < 14):
        print("what would you like to eat", a)

elif(H>=16 and H<20):
    print("Good evening", a)
    print("come home")
else:
    print("Good night")
    print("bye")
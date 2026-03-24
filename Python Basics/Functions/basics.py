def greet():     ## function defination 
    print('Jyoti is a brilliant AI Engineer')

greet()         ## function call


## parameters and arguments
def greet(name):          # parameter
      print('Hello', name)

greet('Jyoti')            # argument


## Return values  ->  function se value vapis lena
def add(a,b):
    return a+b

result = add(2, 3)
print(result)


## multiple return value
def calculate(a,b):
     return a + b, a * b, a - b, a/b

result = calculate(8,4)
print(result)


## default parameters
def greet(name = 'guest'):
     print('hello', name)
             
greet()         # hello guest
greet('Jyoti')  # hello Jyoti


## keyword arguments
def student(name, age):
     print(name, age)

student('Jyoti', 21)
student(21,'Jyoti')     # order matters
student(age = 21, name = 'Jyoti')



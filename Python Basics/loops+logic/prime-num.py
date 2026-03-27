def is_prime(num):

    for i in range(2,num):
        if num%i == 0:
            return 'not prime'
    return 'prime'
        
num = int(input())
print(is_prime(num))
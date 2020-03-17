import random;

def calc_check_digit(number):
    return str((10 - sum((3, 1)[i % 2] * int(n)
                         for i, n in enumerate(reversed(number)))) % 10)
    
code = '742'
for i in range(9):
   code = code + str(random.randint(0, 9))     
    
print(code + calc_check_digit(code))
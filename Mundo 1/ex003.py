cores = {'clean':'\033[m', 
        'blue':'\033[34m', 
        'red':'\033[31m', 
        'yell':'\033[33m', 
        'grey':'\033[32m'}
print('Vamos fazer matemática!')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
p = n1 + n2
print('A soma entre {}{}{} e {}{}{} vale {}{}{}'.format
(cores['red'], n1, cores['clean'], 
cores['blue'], n2, cores['clean'], 
cores['yell'], p, cores['clean']))
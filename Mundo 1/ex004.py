cores = {'red':'\033[31m', 
        'green':'\033[32m',
        'yell':'\033[33m',
        'blue':'\033[34m',
        'purple':'\033[35m',
        'cyan':'\033[36m',
        'clean':'\033[m'}
x = input('Digite algo: ')

print('{}tipo: {}{}'.
      format(cores['red'], cores['clean'], type(x)))
print('{}É alfanumérico?: {}{}'.
      format(cores['yell'], cores['clean'], x.isalnum()))
print('{}É numérico: {}{}'.
      format(cores['green'], cores['clean'], x.isnumeric()))
print('{}É alfabético?: {}{}'.
      format(cores['cyan'], cores['clean'], x.isalpha()))
print('{}Está somente em maiúsculas?: {}{}'.
      format(cores['blue'], cores['clean'], x.isupper()))
print('{}Está somente em minúsculas?: {}{}'.
      format(cores['purple'], cores['clean'], x.islower()))
print('{}Está capitalizada?: {}{}'.
      format(cores['red'], cores['clean'], x.istitle()))
print('{}Possui somente espaço?: {}{}'.
      format(cores['yell'], cores['clean'], x.isspace()))


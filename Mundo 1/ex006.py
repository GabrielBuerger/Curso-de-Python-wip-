n = int(input('Digite um número: '))
#1º Jeito:
# d = n*2
# t = n*3
# rq = n**1/2
# print('Seu dobro é: ', d)
# print('Seu triplo é: ', t)
# print('Sua raíz é: ', rq)
#2º Jeito:
print('Seu dobro é: {}'.format(n*2))
print('Seu triplo é: {}'.format(n*3))
print('Sua raíz é: {:.3f}'.format(pow(n, 1/2)))
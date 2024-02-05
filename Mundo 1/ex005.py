n = float(input('Digite um número:'))
#Método 1:
# s = int(n + 1)
# a = int(n - 1)
# print('Seu sucessor é:\033[35m', s, '\033[m')
# print('Seu antecessor é:\033[35m', a, '\033[m')
#Método 2:
print('Seu sucessor é {} e seu antecessor é {}'.
      format(n+1, n-1))

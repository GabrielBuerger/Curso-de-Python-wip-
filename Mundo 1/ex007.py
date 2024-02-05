n1 = float(input('Primeira nota do(a) aluno(a): \033[33m'))
n2 = float(input('\033[mSegunda nota do(a) aluno(a): \033[33m'))
media = float((n1 + n2)/2)
print("{}Sua média foi {}{:0.2f}{}".
      format('\033[m', '\033[33m', media, '\033[m'))


n = float(input('Escreva um valor em metros:\033[33m '))
print('''\033[37mKilômetros: \033[33m{}km\033[37m
Hectômetros: \033[33m{}hc\033[37m
Decâmetros: \033[33m{}dc\033[37m
Metros: \033[33m{}m\033[37m
Decímetros: \033[33m{}dm\033[37m
Centímetros: \033[33m{}cm\033[37m
Milimetros: \033[33m{}mm\033[37m'''.
      format(n/1000, n/100, n/10, n, n*10, n*100, n*1000))
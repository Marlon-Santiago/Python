from datetime import date

ano = int(input('Digite o ano em que você nasceu: '))

anoatual = date.today().year


idade = anoatual - ano
alistamentop = idade - 18
alistamentof = 18 - idade

if idade <= 16:
    print(f'Você tem {idade} anos faltam {alistamentof} anos portanto não tem idade para se alistar ainda falta acalma esse coração')

elif idade == 17:
    print('Se você estiver nos 6 primeiros meses do ano que faz 18 anos está na hoara de se alistar')

elif idade == 18:
        print('você se alistou ou deveria se alistar esse ano')
else:
     idade > 18
     print(f'Você deveria ter se alistado a {alistamentop} anos')

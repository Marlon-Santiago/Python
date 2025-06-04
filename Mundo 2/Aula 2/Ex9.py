from datetime import date

ano1 = int(input("Digite o primeiro ano de nacimento: "))
ano2 = int(input("Digite o segundo ano de nacimento: "))
ano3 = int(input("Digite o terceiro ano nacimento: "))
ano4 = int(input("Digite o quarto ano nacimento: "))
ano5 = int(input("Digite o quinto ano nacimento: "))
ano6 = int(input("Digite o sexto ano nacimento: "))
ano7 = int(input("Digite o sétimo ano nacimento: "))

maiores = 0
menores = 0
ano_atual = date.today().year

print(ano_atual)

for ano in (ano1, ano2, ano3, ano4, ano5, ano6, ano7):
    
    if ano_atual - ano >= 18:
        maiores += 1
    
    if ano_atual - ano < 18:
        menores += 1

print(f'dos 7 {maiores} são maior de idade e {menores} são menores de idade')


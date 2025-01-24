a = float(input('Digite a medida da 1 tangencia: '))
b = float(input('Digite a nedida da 2 tangencia: '))
c = float(input('Digite a medida da 3 tangentre: '))

if  a < b + c and b < a + c and c < a + b:
    print('\033[1;32;40m Com as medidas digitadas acima e possivel forma um triangulo [m ')

else:
    print('\33[1;31;40mCom as medidas citadas acima não e possivel formar um triangulo [m')
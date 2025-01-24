a = float(input('Digite a medida de um lado do triangulo'))
b = float(input('digite a medida de outro lado do trinagulo'))
c = float(input('Digite a medida do terveiro lado do triangulo'))

#equilatero = a == b == c
#isoseles = a == b != c or a != b == c
#escaleno = a != b != c


if a < b + c and b < a + c and c < a + b and a == b == c :
    print('É possivel fomar um triangulo equilatero')

elif a < b + c and b < a + c and c < a + b and a == b != c or a != b == c or a == c != b:
    print('É possivel fomar um triangulo isoseles')

elif a < b + c and b < a + c and c < a + b and a != b != c != a:
    print('É possivel fomar um triangulo escaleno')

else:
    print('Com essa medidas não se pode forma um triangulo')
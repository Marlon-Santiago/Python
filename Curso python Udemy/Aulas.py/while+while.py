"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

"""

qtd_linhas = 10
qtd_colunad = 10

linha = 1

while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunad:
        print(f'{linha =}, {coluna =}')
        coluna += 1
        
    linha += 1

print('Acabou')
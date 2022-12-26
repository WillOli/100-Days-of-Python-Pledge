# Instruções
# Escreva um programa que some os algarismos de um número de 2 algarismos. por exemplo. se a entrada foi 35, então a saída deve ser 3 + 5 = 8
# Aviso. Não altere o código nas linhas 1-3. Seu programa deve funcionar para diferentes entradas. por exemplo. qualquer número de dois dígitos.
# Exemplo de entrada
# 39
# Saída de exemplo
# 3 + 9 = 12

digite_dois_numeros = input("Digite dois números inteiros: ")

primeiro_numero = digite_dois_numeros[0]
segundo_numero = digite_dois_numeros[1]

resultado = int(primeiro_numero) + int(segundo_numero)

print(resultado)
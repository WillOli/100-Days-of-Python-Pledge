"""
Você vai escrever um programa que marcará um ponto com um X.

No código inicial, você encontrará uma variável chamada map.

Este map contém uma lista aninhada. Quando map é impresso é assim que a lista aninhada se parece:

[ [ ' ⁇ ️', ' ⁇ ️', '️' '], [ ' ⁇ ️', ' ⁇ ️', ' ⁇ ️' ], [ '️', '️', ' ⁇ ️' ] ]

Isso é um pouco difícil de trabalhar. Então, nas linhas 6 e 23, usamos essa linha de código print(f"{row1}\n{row2}\n{row3}" formatar as 3 listas a serem impressas como um quadrado de 3 por 3, cada uma em uma nova linha.

[ ' ⁇ ️', ' ⁇ ️', ' ⁇ ️' ]

[ ' ⁇ ️', ' ⁇ ️', ' ⁇ ️' ]

[ ' ⁇ ️', ' ⁇ ️', ' ⁇ ️' ]

Agora parece um pouco mais com as coordenadas de um mapa real:

"""
row1 = ["⬜","️⬜","⬜"]
row2 = ["⬜","⬜","️⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
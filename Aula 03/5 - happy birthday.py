# Criar um programa que pergunta o nome de usuário, ano que nasceu e o ano atual.
# O programa deve calcular a idade da pessoa e printar no seguinte formato: "Olá, {nome}! Você tem {idade} anos!"
# Se o usuário tiver mais de 30 anos, o programa deve dizer também: "Nossa! Como você é velho!".
print('Qual é o seu nome:')
name: str = input()
print('Qual o ano que você nasceu:')
birth_year = int(input())
print('Qual é o ano atual:')
date = int(input())

age = date - birth_year

print(f'Olá, {name}! Você tem {age} anos!')

if age > 30:
    print('Nossa como você é velho')

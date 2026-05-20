# Crie um programa que salva uma lista de compras. Ele deve perguntar ao usuario qual item quer adicionar na lista
# Se ele digiar apenas 'q', o programa deve parar de adicionar na lista.
# Depois disso, todos os itens que ele adicionou devem ser printados na tela, assim como a quantidade de items.

l = []
while True:
    print('Qual item você deseja adicionar a lista?')
    item = input()
    if item == 'q':
        break

    l.append(item)

print(f'Os items que você adicionou foram: {l}')
print(f'Você adicionou {len(l)} items.')

# Você tem um filho que gosta de dar nomes diferentes a itens da lista de compra.
# Depois que a lista for criada, pergunta ao usuário para dar nomes especiais a alguns itens.
# Para parar de perguntar ele deve digitar 'q'.
# Quando for printar colocar o nome "especial" ao lado do item, se houver.

renamed = {}

while True:
    print('Que item você deseja renomear?')
    item = input()

    if item == 'q':
        break

    print('Qual é o novo nome?')
    new_name = input()
    renamed[item] = new_name

for to_buy in l:
    item_exist: str | None = renamed.get(to_buy)

    if item_exist is None:
        print(f'Item normal: {to_buy}')
    else:
        print(f'Esse é um item associado: {item_exist}')



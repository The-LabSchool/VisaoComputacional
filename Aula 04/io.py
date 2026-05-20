# Lendo arquivo
with open('numpy.py', 'r') as file:
    # print(file.read())
    ...

# Salvando arquivos
s = "Você está lendo a senha do meu cartão de credito"
with open('senha.txt', 'w') as file:
    file.write(s)

# O que é um JSON (é um dicionario)
import json

d = {
        'nome': 'Fabio',
        'idade': 23,
        "sobrenome": "Marcon"
}

# Salvar um JSO
with open('dados.json', 'w') as file:
    json.dump(d, file)

# Carregando um JSON
with open('dados.json', 'r') as file:
    print(json.load(file))






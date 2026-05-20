# Dictionaries, creating and appending to them
d = {
        'numero': 12
}

print('Um elemento do dict:', d['numero'])
print(d)

d['outro'] = 20
print('O que tem dentro de outro:', d['outro'])

# Retrieving information from them (black magic)
d['test'] = 15

if el := d.get('test'):
    print(f'Esse elemento existe: {el}')
else:
    print('Esse elemento não existe')


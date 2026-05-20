# if and elses
if 12 == 13:
    if 10 == 12:
        print('Isso está dentro do IF')
    else:
        print('Bla bla')
elif 12 == 12:
    print('Whatever')
else:
    print('Isso está fora do IF')

# for loops (range)
print('---------------')
print(f'Isso é um range: {list(range(3))}')
for i in range(3):
    print(i)
print('---------------')

# while loops
while 12 == 13:
    print('Isso será eterno')

# break and continue
for i in range(5):
    if i == 3:
        continue

    print(f'Iter - {i}')

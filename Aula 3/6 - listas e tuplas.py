# Accessing elements in lists, string and tuples
array = [12, 13, 14]
print(array[0])

# Slicing strings, lists and tuples
s = [12, 13, 14]
print(s[0:2])
s = "Fabio Marcon"
pos_space = s.find(' ')

print(s[0:pos_space])

# Add / remove elements from lists
print('----------------------')
this_l = [12, 13, 14]
print(f'Before: {this_l}')
this_l.append(16)
print(f'After: {this_l}')
this_l.remove(16)
print(f'After removal: {this_l}')
print('----------------------')

# Count the amount of elements
print('----------------')
print(f'Quantidade de elementos: {len(this_l)}')
print('----------------')

# Tuples are immutable (little bitches that they are)

# Iterating over lists, tuples and strings
fruits = ["Maça", "Banana", "Cadeira"]
for fruit in fruits:
    print(fruit + "a")

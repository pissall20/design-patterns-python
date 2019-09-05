from tigger import Tigger

a = Tigger()
b = Tigger()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Are they the same object? {a is b}')


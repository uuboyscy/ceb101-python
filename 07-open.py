f = open('./test123.txt', 'r', encoding='utf-8')

print(f.readline())
print(f.readline())
print(f.readline())

print(f.readlines())

f.close()

with open('./test123.txt', 'w', encoding='utf-8') as f:
    f.write('123123\n')
    f.write('321321')



import sys

def add(x, y):
    return int(x) + int(y)

print(add(3, 5))
print(sys.argv)

print(sys.argv[1], sys.argv[2])
print(add(sys.argv[1], sys.argv[2]))
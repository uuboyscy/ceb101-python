import sys

sys.stderr = open('./test-error.txt', 'w')
a = ['1', '2', '3']
# print(a[3])

for i in sys.path:
    print(i)

import sys
import time

print('123')
print('123', file=open('./test123.txt', 'w'))

# f = open('./test123.txt', 'w')
# for i in range(0, 10):
#     print(i, file=f, flush=True)
#     print(i)
#     time.sleep(1)

for i in range(0, 10):
    print(i, file=open('./test1234.txt', 'w'))
    print(i)
    time.sleep(1)

import time

print(time.time())

for i in range(0,10):
    print(i)
    # time.sleep(1)

print(time.localtime())
print(time.gmtime())
print(time.asctime())

print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
from multiprocessing.dummy import Pool as ThreadPool
import os
import time

def longTime(i):
    print('PID: {}, Task: {} .'.format(os.getpid(), i))
    time.sleep(2)
    result = 10 ** 30
    print('Result: {}'.format(result))
    return 10 ** 30

if __name__ == '__main__':
    start_time = time.time()
    print('母程序PID: {}'.format(os.getpid()))

    p = ThreadPool(4)
    # for i in range(0, 8):
    #     p.apply_async(longTime, args=(i, ))
    data = p.map(longTime, iterable=range(0,8))
    p.close()
    p.join()

    print(data)

    end_time = time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))
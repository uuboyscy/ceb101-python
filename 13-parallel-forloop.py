import time
import os
import multiprocessing

def longTime(i):
    print('PID: {}, Task: {} .'.format(os.getpid(), i))
    time.sleep(2)
    result = 10 ** 30
    print('Result: {}'.format(result))

if __name__ == '__main__':
    # 開始時間
    start_time = time.time()
    print(os.getpid())

    work = []
    for i in range(0, 30):
        work.append(multiprocessing.Process(target=longTime, args=(i, )))

    for i in range(0, 30):
        work[i].start()

    for i in range(0, 30):
        work[i].join()

    end_time = time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))
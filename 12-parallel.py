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

    # 假設該任務需要執行 4 次
    # for i in range(0,4):
    #     longTime(i)

    work1 = multiprocessing.Process(target=longTime, args=(1, ))
    work2 = multiprocessing.Process(target=longTime, args=(2, ))
    work3 = multiprocessing.Process(target=longTime, args=(3, ))
    work4 = multiprocessing.Process(target=longTime, args=(4, ))

    work1.start()
    work2.start()
    work3.start()
    work4.start()

    work1.join()
    work2.join()
    work3.join()
    work4.join()

    end_time = time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))
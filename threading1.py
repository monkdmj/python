#!/
#
"""[summary]

[description]
"""

import threading
from time import sleep, ctime

loop = [4, 2]


def _loop(loop, nsec):
    print('start', loop, ctime())
    sleep(nsec)
    print('end', loop, ctime())


def main():
    print('start:', ctime())
    loops = range(len(loop))
    threads = []
    for i in loops:
        lock = threading.Thread(target=_loop, args=(i, loop[i]))
        threads.append(lock)
    for i in loops:
        threads[i].start()
    for i in loops:
        threads[i].join()
    print('Done:', ctime())


if __name__ == '__main__':
    main()

def openfile1():
    try:
        f = open('test.txt', 'r')  # \可以用于一行代码未写完
        print(f.read())
    finally:
        if f:
            f.close()


def openfile2():
    with open('test.txt', 'r') as f:
        print(f.read())


def openfile3():
    with open('test.txt', 'r') as f:
        print(f.readline())
        print('test')
        print(f.readlines())


'''
3425435435

test
['fdssss\n', 'rtttttttttttt\n', 'fdgdfg\n', 'end']
'''


def openfile4():
    with open('test.txt', 'r') as f:
        print(f.read(4))
        print(f.read(4))
        print(f.read(4))


'''
3425
4354
35
f
'''


def openfile5():
    with open('test.txt', 'r') as f:
        for line in f.readlines():
            print(line.strip())
            print(line)


'''
3425435435
3425435435

fdssss
fdssss

rtttttttttttt
rtttttttttttt

fdgdfg
fdgdfg

end
end
'''

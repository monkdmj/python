def foo(s):
    n = int(s)
    print('raise ?start')
    if n == 0:
        raise ValueError('invalid value: {}'.format(s))
        '''
        在外面那个函数当中你把问题给捕获了（except），所以编
        译器就不会报错给你此traceback
        '''
    print('raise ?go on')
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
    '''
    在bar()中把raise注释后，虽然此时bar()中捕获到了foo()抛出的异常，但是只做了
    print('ValueError!')操作,并没有继续把错误往上抛出，这样外部就会认为这个异
    常被bar()自己处理掉了。所以不会打印foo()中的错误信息，如果不注释raise，那
    就理解为bar()本身没有能力处理这个异常，继续抛出给自己的上级，因为上级没有
    东西了，所以就在运行结果中抛出来显示了
    '''
    print('except ? go on')

bar()


'''
#print result
raise ?start
ValueError!
Traceback (most recent call last):
  File "C:/WORKSPACE/Python/test/exception1.py", line 17, in <module>
    bar()
  File "C:/WORKSPACE/Python/test/exception1.py", line 11, in bar
    foo('0')
  File "C:/WORKSPACE/Python/test/exception1.py", line 5, in foo
    raise ValueError('invalid value: {}'.format(s))
ValueError: invalid value: 0
'''

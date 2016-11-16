def powe(x,y,*others):
    if others:
        print('zz')
    else:
        return pow(x,y)

def combine(param):
    print(param+globals()['param'])#','有空格

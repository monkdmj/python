class Athlete:

    def __init__(self, aname, abob=None, atime=[]):
        self.name = aname
        self.bob = abob
        self.time = atime

    def top3(self):
        return()


def get_data(filename):
    try:
        with open(filename, 'r') as f:
            dat = f.readline()
        lista = dat.strip().split(',')
        return(Athlete(lista.pop(0), lista.pop(0), lista))
    except IOError as ef:
        print('file error', ef)
        return None


james = get_data(r'C:\WORKSPACE\Python\test\test.txt')
print("hhh")

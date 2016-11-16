"""Framework for getting filetype-specific metadata.

Instantiate appropriate class with filename.  Returned object acts like a
dictionary, with key-value pairs for each piece of metadata.
    import fileinfo
    info = fileinfo.MP3FileInfo("/music/ap/mahadeva.mp3")
    print "\\n".join(["%s=%s" % (k, v) for k, v in info.items()])

Or use listDirectory function to get info on all files in a directory.
    for info in fileinfo.listDirectory("/music/ap/", [".mp3"]):
        ...

Framework can be extended by adding classes for particular file types, e.g.
HTMLFileInfo, MPGFileInfo, DOCFileInfo.  Each class is completely responsible for
parsing its files appropriately; see MP3FileInfo for example.
"""
import os
import sys

def stripnulls(data):
    ''
    return data.replace('\00','').strip()

class FileInfo(dict):
    ''
    def __init__(self, filename=None):
        super(FileInfo,self).__init__()
        self['name'] = filename

    def __getitem__(self, key):
        print('test getitem')
        return self[key]

    def __setitem__(self, key, item):
        self[key] = item

  
class MP3FileInfo(FileInfo):
    ''
    tagDataMap = {"title"   : (  3,  33, stripnulls),
                  "artist"  : ( 33,  63, stripnulls),
                  "album"   : ( 63,  93, stripnulls),
                  "year"    : ( 93,  97, stripnulls),
                  "comment" : ( 97, 126, stripnulls),
                  "genre"   : (127, 128, ord)
                  }

    def __parse(self,filename):
        ''
        self.clear()
        try:
            fsock = open(filename,'rb',0)

        except IOError:
            pass
        

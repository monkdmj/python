#ORM:object relational mapping 对象-关系映射
#把关系数据库的一行映射为一个对象，也就是一个类对应一个表
#ORM框架所有的类只能动态定义
#定义一个User类来操作对应的数据库表User
class Field(object):#保存数据库表的字段名和字段类型
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self):
        return '<%s:%s>'%(self.__class__.__name__,self.name)#输出<对象所属的类名:对象的名字>

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):#当前metaclass方法准备创建的类的对象，类的名字，类继承的父类集合，类的方法集合
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)#封锁对Model的修改，类名是Model就只能返回
        print('Found model:%s'%name)
        mappings=dict()#新建一个字典
        for k,v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
        #v是属于Field类的，因此v遇到print会自动调用__str__ attr是无序的字典，因此打印输出的时候也是无序的
                mappings[k] = v
        # 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，
        # 同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系，这属于User标的属性
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)#属性修改完毕后返回

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self,key):#实例.属性的时候自动调用
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute'%s'"%key)
    def __setattr__(self,key,value):
        self[key]=value
    def save(self):
        fields=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql='insert into %s(%s) values(%s)'%(self.__table__,','.join(fields),','.join(params))
        print('SQL:%s'%sql)
        print('ARGS:%s'%str(args))
class User(Model):
    # 定义类的属性到列的映射
    id=IntegerField('id')#用IntegerField初始化User类的属性，调用setattr自动赋值
    name=StringField('username')
    email=StringField('email')
    password=StringField('password')
#创建一个实例
u=User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
#保存到数据库
u.save()
#创建实例的时候调用Model的方法->调用ModelMetaclass的方法

#无参数
fn1 = lambda:100
print(fn1())

#一个参数
fn1 = lambda a: a
print(fn1('hello world'))

#默认参数
fn1 = lambda a,b,c=100 : a+b+c
print(fn1(10,20))


#可变参数 *args
fn1 = lambda *args:args
print(fn1(10,20,30))
#这里的可变参数传入到lambda之后，返回值为元组

#可变参数 **kwargs
fn1 = lambda **kwargs: kwargs
print(fn1(name='python',age=20))
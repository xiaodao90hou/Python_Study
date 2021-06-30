import functools

list1 = [1,2,3,4,5]

def fun(a,b):
    return a+b

result = functools.reduce(fun,list1)

print(result) 



#filter 过滤函数 

list2 = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x % 2 ==0

result = filter(func,list2)

print(list(result))
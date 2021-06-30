#带判断的lambda
fn1 = lambda a,b: a if a>b else b
print(fn1(1000,500))


#列表数据按字典key的值排序
students = [
    {'name':'TOM','age':20},
    {'name':'ROSE','age':19},
    {'name':'JACK','age':22}
]

#升序
students.sort(key=lambda x: x['name'])
print(students)

#降序
students.sort(key=lambda x:x['name'],reverse=True)
print(students)
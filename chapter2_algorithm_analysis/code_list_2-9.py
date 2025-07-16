from timeit import Timer

#测量调用空函数的时间
def empty_function():
    pass

t_empty=Timer("empty_function()", "from __main__ import empty_function")
print("调用空函数的时间:", t_empty.timeit(number=1000)*1000,'milliseconds')

def test1():
    l=[]
    for i in range(1000):
        l=l+[i]

def test2():
    l=[]
    for i in range(1000):
        l.append(i)

def test3():
    l=[i for i in range(1000)]

def test4():
    l=list(range(1000))

t1=Timer("test1()", "from __main__ import test1")
print("concat",t1.timeit(number=1000)*1000,'milliseconds')
# print("concat",t1.timeit(),'milliseconds')


t2=Timer("test2()", "from __main__ import test2")
print("append",t2.timeit(number=1000)*1000,'milliseconds')

t3=Timer("test3()", "from __main__ import test3")
print("comprehension",t3.timeit(number=1000)*1000,'milliseconds')

t4=Timer("test4()", "from __main__ import test4")
print("list range",t4.timeit(number=1000)*1000,'milliseconds')
# print("list range",t4.timeit(),'s')



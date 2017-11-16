# print(abs(1))
# print(abs(-2))
# print(abs(3.33))
# print(abs(False))
# # print(abs('str')) error
# print(max(1, 2, 3, -2, True))
#
# print(bool("23"))
# print(int("23"))
#
#
# # 定义函数
#
# def myFirstFun():
#     print("Hello %s" % 'My First Function')
#
#
# def getMulResults(x=1, y=1):
#     return x * y
#
#
# def getDivResults(x=1, y=2):
#     return int(x / y)
#
#
# print(getMulResults())
# print(getMulResults(1, 2))
# print(getMulResults(2, 3))
# print(getMulResults([1, 2, 3, 4], 10))
#
# print(getDivResults(10, 2))
#
#
# def addStart(l=[]):
#     l.append("Start")
#     print(l)
#
#
# addStart()
# addStart()
#
#
# def addNewStart(l=None):
#     if l is None:
#         l = []
#     l.append("Start")
#     print(l)
#
#
# addNewStart()
# addNewStart()
#
#
# # 可变参数函数
# def getMulSum(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = n * n + sum
#     print(sum)
#     return sum
#
#
# getMulSum(3, 3, 3, 3, 3)
#
#
#
# # 关键字参数
#
# def person(name, age, **extra):
#     print('name=', name, ' age=', age, str(extra))
#     print('name:%s age:%s extra:%s' % (name, age, extra))
#
#
# ext = {'a': 1, 'c': 2}
# e = {False: 1, True: 2}  # 关键字函数 中的dict key 不能为非str型参数
# person('leo', 22, city='xian', address='yanta', b="sss")
# person("lee", 23, **ext)
#
#
# # person("lee", 23, **e)  # error
#
# # 命名关键字参数
# def person(name, age, *, city, address):
#     print('name:%s age:%s extra:%s %s' % (name, age, city, address))
#
#
# # 调用方式
# person('leo', 22, city='asd', address='asd')


# 组合函数


def fun(a, b, c=0, *d, **e):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'e=', e)


fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4, 4, 4, 4, 4, e=1, ee=2, eee=3, )

fun(*(1, 2, 2, 23, 3, 3, 13, 4, 3, 432, 4), e1=1, e2=2)


##############################################################
# 练习
# origin fun
def product(x, y):
    return x * y


print(product(1, 2))


# new fun
def product(*nums):
    results = 1
    for i in nums:
        results = results * i
    return results


print(product(1, 2))
print(product(1, 2, 3))
print(product(1, 2, 3, 4))
print(product(1, 2, 3, 4), 5)

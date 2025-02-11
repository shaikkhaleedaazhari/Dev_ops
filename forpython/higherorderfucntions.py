# def sum_num(x):
#     return sum(x)
# def Higher_orderFunction(f,lst):
#     var = f(lst)
#     return var
# result =Higher_orderFunction(sum_num,[1,2,3,4,5])
# print(result)

def square(x):
    return x**2
def cube(a):
    return a**3
def absolute(b):
    return -(b)

def Hof(type):
    if type =='square':
        return square
    elif type == 'cube':
        return cube
    else:
        return absolute
res=Hof('square')
print(res(5))
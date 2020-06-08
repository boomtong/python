def create_num(all_num):
    a, b = 0, 1
    currnet_num = 0
    while currnet_num < all_num:
        yield a   #如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器模板
        a, b = b, a+b
        currnet_num += 1

# 如果在调用create_num的时候，发现这个函数中有yield，那么此时不是调用函数，而是创建一个生成器对象
obj = create_num(10)
obj2 = create_num(2)

ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj2)
print("obj2:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)


def create_num(all_num):
    a, b = 0, 1
    currnet_num = 0
    while currnet_num < all_num:
        ret = yield a
        print("ret.....:", ret)
        a, b = b, a+b
        currnet_num += 1


obj = create_num(10)

ret = next(obj)
print("obj:", ret)

ret = obj.send("hahaha")
print(ret)
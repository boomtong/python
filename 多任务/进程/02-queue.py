import multiprocessing

q = multiprocessing.Queue(3)

q.put("111")

q.put("222")

q.put("333")

print(q.full())


a = q.get()
print(a)
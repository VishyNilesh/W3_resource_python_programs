d = {100:'durga',200:'ravi',300:'shiva'}
print(d)
print(type(d))
d = [(100,'durga'),(200,'shiva'),(300,'ravi')]
print(type(d))
d = dict(d)
print(type(d))
d = [[100,'durga'],[200,'shiva'],[300,'ravi']]
print(type(d))
d = dict(d)
print(type(d))
print(len(d))
print(d.get(100))
del d[100]
print(d.get(100))
print(d.get(100,'Guest'))
d.pop(200)
print(d)
d.popitem()
print(d)
d = dict([(100,'durga'),(200,'shiva'),(300,'ravi')])
print(d.keys())
print(d.values())
print(d.items())
for k,v in d.items():
    print(k,'---',v)
d1=d.copy()
print(id(d))
print(id(d1))
d.setdefault(500,'Nilesh')
print(d)
d.setdefault(100,'ankit')
x = {1000:'a',2000:'b',3000:'c'}
d.update(x)
print(d)
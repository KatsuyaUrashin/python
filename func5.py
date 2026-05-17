def abc(j, *x):
    y = sum(x)
    return y

def xxx(j, **z):
    return z

def zzz(j, KEY=None, jj=None, zzz=None):
    return dict(KEY=KEY, jj=jj, zzz=zzz)

def yyy(j, KEY):
    return KEY

l = [1, 2, 3, 4, 5]
print(abc(*l))
print(abc(2, 2, 3))
print(zzz(1, KEY=44, zzz=3))
print(zzz(1, 44, None, 3))
print(xxx(1))
x ={"KEY": 1,
    "zzz": 3,
    "jj": 2,
    }
print(zzz(1, **x))
print(yyy(1, x))
print(yyy(1, KEY={'a':44, 'b':55}))
# print(yyy(1, KEY=44, jj=2, zzz=3))

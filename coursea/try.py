a="hello bob"
try:
    b=int(a)
except:
    b=-1
print("first", b)
a="123"
try:
    b=int(a)
except:
    b=-1
print("second",b)
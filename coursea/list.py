numlist=list()
while True:
    inp=input("enter the number")
    if inp=='done': break
    value=float(inp)
    numlist.append(value)
avg=sum(numlist)/len(numlist)
print(avg)
    
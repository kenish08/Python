count=dict()
inp=input("enter the words:")
word=inp.split()
for i in word:
    count[i]=count.get(i,0)+1
print("count:",count)

bigcount=0
bigword=0
for word,count in count.item():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
print(bigword,bigcount)
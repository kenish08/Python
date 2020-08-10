count=dict()
name=['ken','gen','yen','pen','ken']
for i in name:
    if i not in count:
        count[i]=1
    else:
        count[i]=count[i] + 1
print(count)
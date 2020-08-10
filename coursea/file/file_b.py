# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
tot=0
count=0
ans=0
fh = open(fname)
for line in fh:
    a=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    num=float(a[21:])
    tot=tot+num
    ans=tot/count
print(ans)
print("Done")


largest = -1
smallest = 999
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        a=int(num)
    except:
       	a=print("Invaild input")
    for i in num:
    	if i > largest:           
            largest = i
    	if i < smallest:
            smallest = i
            
print("Maximum is", largest)
print("Minimum is", smallest)
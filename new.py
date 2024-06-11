'''Can you modify the multiplication table program so
that we get a multiplication table from IO to 1 instead'''

number=int(input("enter a number"))
count = 10
while count >=1:
    product=number*count
    print(number,"x",count,"=",product)
    count=count-1

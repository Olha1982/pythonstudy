fizz= int (input())
buzz= int (input())
c= int (input())
for i in  range(1, 1+c):
    if i%fizz==0 and i%buzz==0:
        print ('FB')
    elif i%fizz==0:
        print ('F')
    elif i%buzz==0:
        print ('B')
    else:
    	print (i)

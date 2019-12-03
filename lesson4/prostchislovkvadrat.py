num= int(input("Enter odd number!: "))
def my_square(num):
    return num ** 2
for j in range(2, num):
    if num % j == 0:
        break 
else: 
    print (num ** 2)
 
   
  
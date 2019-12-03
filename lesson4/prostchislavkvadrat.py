final =[]
x=list (range(1, 100))
def my_square(x):
    return x ** 2
for num in range(2, 100):
    for j in range(2, num):
         if num % j == 0:
              break 
    else: 
        final.append (num)      
squared_numbers = list(map(my_square, final)) 
print (squared_numbers)

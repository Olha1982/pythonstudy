x = list(map(int, input("Enter numbers!: ")))
def my_sum(x):
    the_sum = 0
    for i in x:
        the_sum += i
    return the_sum
print (my_sum (x))

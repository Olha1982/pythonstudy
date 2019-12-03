def my_upper(str):
   return my_upper(str)
def my_lower(str):
   return my_lower(str)

w = ["olga", "anna", "maria"]
m = ['andre', 'daniel']
women = list(map(str.upper, w))
men = list(map(str.lower, m))

print(women)
print(men)
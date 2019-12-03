result = []
atestat = {'Maksim Ivanov': [9, 5 , 8 , 9], 'Pavel Petrov': [3, 8, 4, 9], 'Anna Fedorova': [10, 8, 4, 8]}

t = (atestat.values())
(a, b, c) = t

result = []
for i in t:
    middle = sum(i)/len(i)
    result.append(middle)

atestat ['Maksim Ivanov'] = result[0]
atestat ['Pavel Petrov'] = result[1]
atestat ['Anna Fedorova'] = result[2]
print (atestat)

max_val = max(atestat.values())
min_val = min(atestat.values())

for k, v in atestat.items():
    if v == max_val:
        k:v
        print('the best student', k,'have midle mark =', v)
    if v == min_val:
        k:v
        print('the worst student', k,' have midle mark =', v)


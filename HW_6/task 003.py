# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), 
# применив лямбды, filter, map, zip, enumerate, списочные выражения.

#lst = [1, 2, 5, 7, 2, 3, 6]
#for i in range(1, len(lst)):
#    if lst[i] > lst[i - 1]:
#        print(lst[i], end = ' ')


lst = [1, 2, 5, 7, 2, 3, 6]        
res = []
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        res.append(lst[i])
print(res)
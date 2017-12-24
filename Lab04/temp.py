x = ["a", "c", "b", "d"]
y = ["d", "e", "f"]

x_order = dict()
count = len(x)
for element in x:
    x_order[element] = count
    count = count - 1

y_order = dict()
count = len(y)
for element in y:
    y_order[element] = count
    count = count - 1

result = dict()
for element in x:
    result[element] = x_order[element]

common = 0
for element in y:
    if(result.get(element, 0) != 0):
        common = 1
    result[element] = result.get(element, 0) + y_order[element]

max = 0
for rest, weight in result.items():
    if(weight > max  and  x_order.get(rest, 0) != 0  and  y_order.get(rest, 0) != 0):
        max = weight
        max_rest = rest

if(common):
    result = max_rest
else:
    result = "yelpwich"


print(result)
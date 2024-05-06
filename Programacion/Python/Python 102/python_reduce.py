import functools

num = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, num)
# reduce coge una funcion y dos valores, y una lista
# que serian el primer y segundo valor y asi hasta que termine la lista
# y los suma entre ellos

print(result)



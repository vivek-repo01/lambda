#Write a Python program to square and cube every number in a given list of integers using Lambda.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r = list(map(lambda x : x **2, x))
print(r)

r = list(map(lambda x : x **3, x))
print(r)

#map(lambda x: x**2, x): The map function applies the specified function (in this case, the lambda function lambda x: x**2) to each element of the iterable x. It returns an iterator of the results.
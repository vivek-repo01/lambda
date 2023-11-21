#Write a Python program to filter a list of integers using Lambda.

r = list(filter(lambda x : x%2==0, x))
print(r)

r = list(filter(lambda x : x%2 !=0, x))
print(r)


#lambda x: x % 2 == 0: This defines an anonymous function (lambda function) that takes a single argument x and returns True if x is even (i.e., divisible by 2), and False otherwise.

#filter(lambda x: x % 2 == 0, x): The filter function is used to filter elements from the iterable x based on the given lambda function. It returns an iterator containing only the elements for which the lambda function evaluates to True.

#list(filter(lambda x: x % 2 == 0, x)): Converts the filtered iterator to a list. It creates a list of elements from the iterable x for which the lambda function evaluates to True, i.e., it creates a list of even numbers from the original list.

#r = list(filter(lambda x: x % 2 == 0, x)): Assigns the result of the filtering operation to the variable r.
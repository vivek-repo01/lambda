#Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples:
#[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#Sorting the List of Tuples:
#[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)

#Next, you use the sort method to sort the list of tuples based on the second
# element (marks) of each tuple. The key parameter of the sort method takes a function
# that returns a value that will be used as the sort key. In this case, you use
# a lambda function to specify that the sorting should be based on the second element
# of each tuple (x[1]).


#After this line of code, the subject_marks list will be sorted based on the marks
# in ascending order.

#subject_marks.sort(key = lambda x: x[2])
#print(subject_marks)
#Write a Python program to find if a given string starts with a given character using Lambda.
#Sample Output:
#True
#False

def find_st(text):
    r = lambda text: text[0]
    if text[0]=="a":
        print("True")
    else:
        print("False")

find_st("alpha")

------------------------------------

r = lambda x: True if x.startswith('P') else False
print(r('Python'))
r = lambda x: True if x.startswith('P') else False
print(r('Java'))



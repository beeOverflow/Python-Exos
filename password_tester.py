import re
password = input("Write the password to test: ")
score = 5

if len(password) =< 8 :
    print("Password should be above or equal 8 characters")
    score -=1
lowercase_regex = re.compile(r'[a-z]')   
capital_regex = re.compile(r'[A-Z]')
numbers_regex = re.compile(r'[0-9]')
symbols_regex = re.compile(r'[^a-zA-Z0-9]')
# using look ahead assertion in one go (?=) where it simply checks whether a given pattern exists on a given input , it does not consume the word
strong_password_regex = re.compile(r'^(?=(.*[a-z]){3,})(?=(.*[A-Z]){2,})(?=(.*[0-9]){2,})(?=(.*[!@#$%^&*()\-__+.]){1,}).{8,}$') 

if not lowercase_regex.search(password):
    print("Password should contain at least one lower case letter")
    score -=1


if not capital_regex.search(password)  :
    print("Password should contain at least one capital letter")
    score -= 1

if not numbers_regex.search(password) :
    print("Password should contain at least a number")
    score -= 1

if not symbols_regex.search(password):
    print("Password should contain at least a symbol")
    score -= 1

print("your password score = ",score)
if score == 5 :
    print("thats a strong password")


if strong_password_regex.search(password):
    print('That\'s a strong password :D')


"""
output:

Write the password to test: HelloMum98123#$
your password score =  5
thats a stronger password
That's a strong password :D
"""

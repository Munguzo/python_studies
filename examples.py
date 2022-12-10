#It all starts here
a = 10
b = 15
print('The result will be', a + b)

#playing with inputs
name = input('What is your name? ')
print('Hello ,', name)
birth_year = input('When were you born? ')
age = 2022 - int(birth_year)
print(age, 'is your age.')
input('''Now that we know your age, 
let us do a simple Math with you. Press enter to continue''')
#simple calculator about addition
num1 = input('Enter your number ')
num2 = input('Enter another number ')
result = int(num1) + int(num2)
print('The result is ', result)
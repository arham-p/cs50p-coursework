#Ask user for their name
name = input('Whats your name? ').strip().title()

#Split user's name into first and last name
first, last = name.split(" ")

#Say hello to user
print('Hello, ', end='')
print(name)
print(f'hello, {first}')

#Calculator

x= float(input('What is x? '))
y= float(input('What is y? '))
z=(x/y)

print(f'{z:.2f}')

def main():
    x = int(input('What is x? '))
    print('x squared is', (x))

def square(n):
    return pow(n, 2)

main()

#Make your own function

def hello(to='world'):
    print('Hello,', to)

hello()
name= input('Whats your name? ')
hello(name)



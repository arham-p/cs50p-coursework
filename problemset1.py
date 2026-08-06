#Deep Thought

user = input('What is the Answer to the Great Question of Life, the Universe and Everything? ')

if user == 'Forty-two' or user == '42' or user == 'Forty-Two' or user == 'Forty Two' or user == 'Forty two' or user == 'forty-two' or user == 'forty two':
    print('Yes')
else:
    print('No')

#Home Federal Savings Bank

user2 = input('Please enter a greeting: ')

step2 = user2.strip()

step3 = step2.lower()

if step3.startswith('hello'):
    print('$0')
elif step3.startswith('h'):
    print('$20')
else:
    print('$100')

#File Extensions

user = input('Please enter your file name: ')

next = user.lower()

if next.endswith('.gif'):
    print('image/gif')
elif next.endswith('.jpg') or next.endswith('.jpeg'):
    print('image/jpeg')
elif next.endswith('.png'):
    print('image/png')
elif next.endswith('.pdf'):
    print('application/pdf')
elif next.endswith('.txt'):
    print('text/plain')
elif next.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')

#Math Interpreter

user = (input('Please type your arithmetic expression with one space on both sides of the arithmetic sign: '))
parts = user.split()
first = int(parts[0])
second = (parts[1])
third = int(parts[2])

if second == '+':
    equation = first + third
elif second == '-':
    equation = first - third
elif second == '*':
    equation = first * third
elif second == '/':
    equation = first / third

print(f'{equation:.1f}')

#Meal Time

def convert(time):
    parts = time.split(':')
    one = int(parts[0])
    two = int(parts[1])
    three = two/60
    four = float(three)
    return four + one

def main():
    user1 = input('Please enter your time: ')
    user = convert(user1)
    if 7 <= user <= 8:
        print('breakfast time')
    elif 12 <= user <= 13:
        print('lunch time')
    elif 18 <= user <= 19:
        print('dinner time')

main()
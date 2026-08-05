x = int(input('What is X? '))
y = int(input('What is Y? '))

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x is equal to y')

if x != y:
    print('x is not equal to y')
else:
    print('x is equal to y')

score = int(input('Score: '))

if score >= 90 and score <= 100:
    print('Grade: A')
elif score >= 80 and score <90:
    print('Grade: B')
elif score >= 70 and score < 80:
    print('Grade: C')
elif score >= 60 and score < 70:
    print('Grade: D')
else:
    print('Grade: F')

z = int(input('What is Z? '))

if z % 2 == 0:
    print('Even')
else:
    print('Odd')

def main():
    z = int(input('What is Z? '))
    if is_even(z):
        print('Even')
    else:
        print('Odd')

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#match:

name = input('Whats your name? ')

match name:
    case "Harry" | "Ron" | 'Hermoine':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who?')
#Indoor Voice

word = input("What is your name? ")
print(word.lower())

#Playback Speed

phrase = input('What course is this? ')
print(phrase.replace(" ", "..."))

#Making Faces

def convert(text):
    newstring = text.replace(':)', '🙂')
    newstring2 = newstring.replace(':(', '🙁')
    return newstring2
    

def main():
    emoji = input('How are you feeling right now? ')
    print(convert(emoji))

main()

#Einstein

user = int(input('Please enter mass '))
energy = (user) * 300000000 * 300000000
print(energy)

#Tip Calculator

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    e = d.strip('$')
    f = float(e)
    return(f)


def percent_to_float(p):
    q = p.strip('%')
    r = float(q)
    s = r/100
    return(s)


main()
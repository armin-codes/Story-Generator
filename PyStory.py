import time

# Don't click on this -> https://twitter.com/ArminS56183 Enjoy your creative stories!
# and share your opinions with us on Twitter!

print('\nin the year of...\n')
time.sleep(1)

year = input("Enter the story's year\n: ")

while year == '':
    print('Uh come on!! tell us the year!.\n')
    time.sleep(0.5)
    year = input(": ")

time.sleep(0.6)

print(f"\nin the year of {year}, There was a...\n"
      )

gender = input("Enter the character's gender \n: ")

while gender not in ['man', 'woman']:
    doubt = input("Do you really want to be something other than human? \n1. Yes\n2. No\n: ")
    time.sleep(1)
    if doubt == '1':
        print('0k...')
        time.sleep(0.5)
        break
    elif doubt == '2':
        print('Then...')
        time.sleep(0.5)
        gender = input("Enter the character's gender\n1. Man\n 2. Woman\n: ")

time.sleep(0.3)

print(f'\nThere was a {gender} called...\n')

name = input("Enter the character's name:\n")
cap_name = (name.capitalize())
while name == '':
    print('Sorry... What??\n')
    name = input("Enter the character's name:\n")

time.sleep(0.5)

print(f'\nin the year of {year} There was a {gender} called {cap_name}\n')
time.sleep(1)

print(f'{cap_name} lived in...')
places = [1, 2, 3]

while True:
    try:
        live = int(input('''
1. Town
2. City
3. Village
: '''))
        if live not in places:
            raise ValueError('Invalid input')
    except ValueError:
        print('Where??')
    else:
        break

if live == 1:
    live = 'Town'
elif live == 2:
    live = 'City'
elif live == 3:
    live = 'Village'
country = input(f"What's the name of the {live}?")

while country == '':
    print(f"Come on!! Tell us where {name} lives.")
    country = input('Enter the country name\n:')
time.sleep(1)
print(f'\n{name.capitalize()}...\n')
time.sleep(2)
friends_amount = ['1', '2']

friend = input(f'How many friends {name} has?\n1. zero\n2. one\n:')
while friend not in friends_amount:
        print('Invalid input. Please enter one of the following options: zero, one.\n')
        friend = input(f'How many friends {name} has?\n1. zero\n2. one\n:')
if friend == '1':
    print(f'{name} has no friend')
else:
    friend = input(f'{name} had a friend called... \n: ')
    print(f'{name} has a friend called {friend}\n')

go = input(f"""{name} wanted to:
1. Go to work
2. Go to friend's place
3. Go to the jungle
4. Send a mail to {friend}
5. Go around the {live}""")

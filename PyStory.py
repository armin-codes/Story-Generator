import time

# Don't click on this -> https://twitter.com/ArminS56183 Enjoy your creative stories!
# and share your opinions with us on Twitter!

print('in the year of...\n')
time.sleep(1)
while True:
    try:
        year = input("Enter the story's year\n: ")
        time.sleep(0.5)
        if year == '':
            raise ValueError('Invalid input')
    except ValueError:
        time.sleep(0.5)
        print('When??')
    else:
        break

print(f"\nin the year of {year}, There was a...\n")
time.sleep(1)

genders = ['1', '2']
while True:
    try:
        gender = input("Enter the character's gender \n1. Man\n2. Woman\n: ")
        if gender not in genders:
            raise ValueError("Invalid input")
        time.sleep(1)
    except ValueError:
        print("Gender must be 1 or 2 (means man or woman)")
    else:
        break
if gender == '1':
    gender = 'man'
elif gender == '2':
    gender = 'woman'
time.sleep(0.5)
print(f'\nThere was a {gender} called...\n')
time.sleep(0.5)
while True:
    try:
        name = input("Enter the character's name\n: ")
        time.sleep(0.5)
        if name == '':
            raise ValueError('Invalid input')
    except ValueError:
        print('Who??')
    else:
        break
cap_name = (name.capitalize())
time.sleep(0.5)

print(f'\nin the year of {year} There was a {gender} called {cap_name}\n')
time.sleep(0.5)

print(f'\n{cap_name} lived in...\n')
places = [1, 2, 3]

while True:
    try:
        live = int(input(f'''Where did {name} lived?
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

while True:
    try:
        country = input(f"What's the name of the {live}?\n: ")
        if country == '':
            raise ValueError('Invalid input')
    except ValueError:
        print(f"Come on!! Tell us where {name} lives.")
    else:
        break

time.sleep(1)
print(f'\n{name.capitalize()}...\n')
time.sleep(2)
while True:
    try:
        friend_amount = input(f'How many friends {name} has?\n1. zero\n2. one\n: ')
        if friend_amount not in ['1', '2']:
            raise ValueError('Invalid input')
    except ValueError:
        input('No friends or One friend?\n')
        time.sleep(0.5)
    else:
        break
if friend_amount == '1':
    print(f'{name} has no friend')
elif friend_amount == '2':
    print(f'{name} has a friend called...\n')
    time.sleep(0.5)
    while True:
        try:
            friend = input("What's the friend's name\n: ")
            if friend == '':
                raise ValueError('Invalid input')
        except ValueError:
            print('Who??')
        else:
            break
go = input(f"""
{name} wanted to 
1. Go to work
2. Go to friend's place
3. Go to the jungle
4. Send a mail to {friend}
5. Go around the {live}\n: """)

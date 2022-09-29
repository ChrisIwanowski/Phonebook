
user_name = input('Please enter your name: ')
print(f'Hello {user_name}, I am your phone book.')

user_age = (input('Please provide your age: '))

if user_age.isnumeric():
    user_age = int(user_age)
else:
   print('That doesn\'t seem to be an integer')
   exit()

if user_age <= 18:
    print('You are so young! Life is ahead of you!')
elif 40 > user_age > 18:
    print('That\'s a nice age!')
elif user_age >= 40:
    print('you must be very wise!')
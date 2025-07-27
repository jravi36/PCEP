user_age = int(input('Enter your age: '))
user_country = input('Enter your country: ')
if not user_country == 'India' and user_age < 25 or user_country == 'India' and user_age < 23:
    print('You Qualify')
else:
    print('Not Qualified!!')
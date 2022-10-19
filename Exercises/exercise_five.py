
age_user = int(input('How old are you?: '))
incomes_user = int(input('What is your incomes per month?: '))

if age_user > 18 & incomes_user > 1500:
    print('You can pay taxex')
else:
    print('You cant pay taxes')
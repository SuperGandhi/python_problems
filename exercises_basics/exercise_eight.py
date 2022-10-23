amount = float(input('Amount to invest: '))
interest = float(input('Porcentual interest annual : '))
years =  int(input('Years: '))

for i in range(years):
    amount *= 1 + interest / 100
    print('Capital rest: ' + str(i+1) + ' years: ' + str(round(amount, 2)))
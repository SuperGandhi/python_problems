# Finding the average of N numbers in Python

number = int(input("How many numbers ? "))
total = 0

for n in range(number):
    numbers =  float(input("Enter any number: "))
    total += numbers 
    
average = total / number
print (f'Average is : {average}')
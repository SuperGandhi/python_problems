name_user = input('What is your name? : ')
genre_user = input('What is your genre? : ')

if genre_user == "M":
    if name_user.lower() < 'm':
        group = "A"
    else:
        group = "B"

else:
    if name_user.lower() > "n":
        group = "A"
    else:
        group = "B"
        
print('Your group is: ' + group)



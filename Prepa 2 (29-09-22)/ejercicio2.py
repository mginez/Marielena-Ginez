password = [input('Please enter your password: ')]
is_valid = False
alpha = False
number = False

while is_valid == False:
    while len(password) < 8 or password.islower() == True or password.isupper() == True or alpha == False or number == False:
        password = input('Not valid. Try a new password: ')
        
        while alpha == False and number == False:
            for letter in password:
                if letter.isalnum() == True:
                    alpha = True
                elif letter.isnumeric() == True:
                    number = True
                else:
                    password = input('Not valid. Try a new password: ')
    is_valid = True
print('Password saved')
                




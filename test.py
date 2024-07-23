Username = input(print('enter a username, it must have less than 20 chracters'))
z = 1
while z == 1:
 if len(Username) < 21: z = 2, print(Username)
 else: Username = input(print('your username is too long, please try entering something with less than 20 characters'))
Password = input(print('Enter a password, It must have 8 characters, one uppercase character, one special character and have less than 20 characters'))
y = 1
while y == 1: 
 if len(Password) > 7 and len(Password) < 21 and any(x.isupper() for x in Password) and any(not x.isalnum() for x in Password): y = 2, print (Password)
 else: Password = input(print('Your password information is incorrect. It must have 8 characters, one uppercase character, one special character and have less than 20 characters'))
def valid_input(inp):
    try:
        ret=int(inp)
        if not 0<ret:
            print ("Less than 0! Try Again")
            return None
        return ret
    except:
        print ("Invalid input!! Try Again")
        return None
while True:
    Age=valid_input(input("Enter your age, make sure it is above 0"))
    if Age:break
print(Age) 
Email = input("enter your email address")
h = 1
while h == 1:
  if Email.endswith("@gmail.com" or "@hotmail.com" or "@outlook.com" or "@yahoo.com" or "@icloud.com"): h = 2, print(Email)
  else : Email = input("enter a valid email address")

print(Username, Email, Password, Age )
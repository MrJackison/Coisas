from random import choice #import choice to chose a characters from the strings to make the password
#Password generator

nChar = int(input("Number of characters: "))

#Characters to use
aLetters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
Aletters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
numbers = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0")
symbols = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","&","*")

# Method to generate the password according to the nChar and lComp
def generator (nChar, lComp):
        password = []
        if lComp == 1:
            for i in range (nChar):
             password.append(choice(aLetters))
        elif lComp == 2:
            for i in range (nChar):
              password.append(choice(Aletters))
        elif lComp == 3:
            for i in range (nChar):
              password.append(choice(numbers))
        elif lComp == 4:
            for i in range (nChar):
              password.append(choice(symbols))
        return password

# Loop to confirm that the user entered a valid number, otherside the program will restart
while True:
    lComp = int(input("Level of complexity:\n1= a 2= aA 3= aA1 4= aA1?:\n"))  
    if lComp not in [1,2,3,4]:
        print("\nError! Enter a number from 1 to 4\n")
    else:
        password = generator (nChar, lComp)
        print("Your Password:")
        for c in password:
          print(c, end="")
        print("\n")
        break

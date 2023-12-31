from os.path import exists
import secrets
import string

def generatePass():
    lettersU = string.ascii_uppercase
    lettersL = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    alphabet = lettersU + lettersL + digits + special_chars
    
    pwd_length = 8
    
    pwd = ""
    while True:
        for x in range(pwd_length):
            pwd += "".join(secrets.choice(alphabet))
            
        if (any(char in special_chars for char in pwd) 
            and any(char in digits for char in pwd)>=1
            and any(char in lettersU for char in pwd)>=1
            and any(char in lettersL for char in pwd)>=1):
            f = open("passwords.txt", "w")
            f.write(pwd)
            f.close()
            break
        pwd = ""

def main():
    generatePass()
main()
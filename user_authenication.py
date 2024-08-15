import hashlib

# This the backend for the user login page 
# It includes the sign in, register and some user classes

# the function for signing into the weather app

        
invalid_strings = [",","-","=","+","{}","{","}","'",'"','/']

def sign_in(username:str, password:str):
    with open('registered_users.txt', 'r') as fin: # accesses the registered users text file for 
                                                    # for reading the registered users
        for line in fin:
            splitted_line = line.strip().split(",")
            u = splitted_line[0] #takes in the username
            p = splitted_line[1] # takes in the password
            
            if u == username and p == str(hashlib.sha256(password.encode()).hexdigest()): # Compares input with stored usernames and passwords
                                                # to check if you're teh user
                print("You are signed in")
                return True
        print("The password and username don't match. Try Again!")
        print(f"p={p} type = {type(p)}\npassword={hashlib.sha256(password.encode())} type = {type(hashlib.sha256(password.encode()).hexdigest())}")
        return False

# This the function to register the suers onto the weather app
def register(username: str, password:str):
    with open('registered_users.txt', 'r') as fin:

        for character in invalid_strings:
            if character in username:
                return "wrong"

        for line in fin:
            splitted_line = line.strip().split(",")
            u = splitted_line[0]
            
            if u == username:
                print("Username already in use. Try Again!")
                return "taken"
    
    with open('registered_users.txt', 'a') as fout: # this will open the text file to write the registered usernames 
                                                    # into the text file 
        fout.write(f"{username},{hashlib.sha256(password.encode()).hexdigest()}\n")
        print("Thanks for registering")
        return True


correct_uername = "admin"
correct_password = "1234" # let it be a string (str) so the input command will be string

user_name = "" # initial is blank, no input has been made
password = "" 
attempt = 0 # no attempt has been made yet
max_attempt = 3 # user has 3 attempt before accont is locked for incorrect entry

while attempt < max_attempt: # this checks if the number of attempts has been exceeded
    user_name = input("Enter username: ") 
    password = input("Enter password: ")
    
    if user_name.lower() == "" or password == "": # this makes it not to be case sensitive
        print ("Username or password can not be empty") # there shoudn't be augmented operation here, since no input resulting in no attempt
    elif user_name.lower() != correct_uername or password != correct_password: # can also be written as not(user_name == correct_uername and password == correct_password)
        attempt += 1 # this will be increasing the number of attempt by 1 each time an attempt is made
        print ("Invalid username or password")
        print (f"Attempt left: {max_attempt - attempt}")
    elif user_name.lower() == correct_uername and password == correct_password:
        print ("login successful")
        break # this will stop the loop
if attempt == max_attempt:
    print ("Account locked")

# Continuous Even or Odd Checker

while True:
    # Ask the user to enter a number or 'q' to quit
    user_input = input("Enter a number (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if user_input.lower() == 'q': # .lower() makes the inputed string to be lowercase if uppercase 
        # it can also be writen as "if user_input == 'q' or user_input == 'Q'"
        print("Exiting program. Goodbye!")
        break  # Exit the loop
    
    # Convert input to integer and check even/odd
    try:
        num = int(user_input)
        if num % 2 == 0:
            print(f"{num} is an even number")
        else:
            print(f"{num} is an odd number")
    except ValueError:
        print("Invalid input! Please enter a valid number or 'q' to quit.")
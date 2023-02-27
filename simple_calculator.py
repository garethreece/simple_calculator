# Calculator task - calculator adds, subtracts, multiplies, and divides two numbers
# It saves the information to files and will allow the user to view the saved calculations

# *** define functions ***
# This function shows the information to explain how a user can choose a filename or go with a default.
# This will return the filename text back to the main program
def get_filename():
    filename = input(f"""
Enter a filename to save the calculations.
Filename conditions:
    - Less than 20 characters
    - Letters and numbers only
    - Just the filename - No extension (.txt)
If you leave it blank the filename \'calculations.txt\' will be used.
Filename: """)
    return filename

# If the filename is less than 20 charatcers, it will be accepted
# This is an arbitary figure and could be changed, I just chose something so that filename sizes didn't get silly 
def check_filename_length():
    if len(filename) < 20:
        return True
    else:
        print("This filename is too long please try something shorter")
        return False

# Symbols can mess up programs and filenames, so I thought I would makes sure no symbols were being used.
# This function checks that only numbers and letters are used
def check_filename_symbol():
    if filename.isalnum() == True:
        return True
    else:
        print("This filename contains symbols or spaces, please try again.")
        return False

# If the file name already exists, it checks with the user that this is okay before over writting any file.
# The function trys to open the filename given, if it can it closes it and reports back that it exists.
# If it doesn't the except rule filenotfounderror is used, but this is okay and will continue. 
def check_file_exists():
    file = None
    try:
        file = open(filename, "r", encoding = "utf-8-sig")
        return True
    except FileNotFoundError:
        return False
    finally:
        if file is not None:
            file.close()

# funtion to open and return the ability to write new file
def write_file():
    return open(filename, "w+", encoding = "utf-8-sig")

# function to open and return the ability to append text to the end of the file
def append_file():
    return open(filename, "a", encoding = "utf-8-sig")

# function to open and read only the file
def read_file():
    return open(filename, "r", encoding = "utf-8-sig") 

# function to show information on a menu about what a user would like to do, and return the selection
def main_menu():
    menu_selection = input("""What would you like to do:
1) Calculation
2) View previous calculations
0) Save calculations and exit
Please select an option 1, 2, or 0 to exit: """)
    return menu_selection

# This function was used twice once for the first number and again for the second number. This saves the amount of code needed.
# It returns both num 1 and num 2 when requested.
def number():
    while True: # This loops makes sure a number is entered, if not it will try again
        num = input("Enter a number: ")
        try:
            num = float(num)
            break
        except ValueError:
            print("Not a number, please try again")
    # if the number entered can be divided by 1 without having a remainder, it is an integer.
    # so to save memory and make the format nice, then if it is an integer, I can define the variable as such
    # I could have used a try except here but that would have used more lines of code.
    if num % 1 == 0:
        num = int(num)
    return num

# the operation() function displays the menu of options you can do to the numbers so the user can select which one they want
# This will return the option selected to the main program
def operation():
    operation_selection = input(f"""
    What operation would you like to do to number 1 {num1} and number 2 {num2}:
        Option 1 - add      ({num1} + {num2})
        Option 2 - subtract ({num1} - {num2})
        Option 3 - multiply ({num1} x {num2})
        Option 4 - divide ({num1} ÷ {num2})
    Please choose a number between 1 - 4: """)
    return operation_selection

# The do_calculation function will take the operation selected and process them on the numbers given
# This will return the answer and operator variables to the main program in the one function
def do_calculation():
    if select_operation == '1':
        answer = add_num()
        operator = "+"
    elif select_operation == '2':
        answer = subtract_num()
        operator = "-"
    elif select_operation == '3':
        answer = multiply_num()
        operator = "x"
    elif select_operation == '4':
        answer = divide_num()
        operator = "÷"
    return answer, operator # these two variables can be returned to the main program

# add a number function that returns the answer to the addition of the two numbers
def add_num():
    answer = num1 + num2
    return answer

# subtract a number function that returns the answer to the subtraction of the num 1 - num 2
def subtract_num():
    answer = num1 - num2
    return answer

# multiply numbers function that returns the answer to the multiplication of the two numbers
def multiply_num():
    answer = num1 * num2
    return answer

# divide the numbers function that returns the answer to dividing num 1 by num 2.
# However if num 2 is a 'zero' then it will return the answer "error can't divide by zero".
def divide_num():
    if num2 == 0:
        answer = "Error: Can\'t divide by zero"
    else:
        answer = num1 / num2
    return answer

# This function will save an answer to the file after every calculation
# It opens and closes the file all in one function
# If file not found it will create a new one and then finally close in eitehr circumstance.
def answer_saved_to_file():
    try:
        file = append_file()
        file.write(f"{print_calc}")
    except FileNotFoundError:
        print("\nFile not found, can't write information!")
        print("A new file will be created and calculation saved from this point on!\n")
        file = write_file()
        file.write(f"{print_calc}")
    finally:
        file.close()


# This will show the file information if chosen in one of the options.
# It reads what is currently on the file and displays it in an easy to read format
# If the file is missing it will state than the error has occured but won't crash the program
# If there is no file it will create a file to write to again.
def show_file():
    try: # If the file is there and it can read it, it will carry on
        file = read_file()
    # If for some reason the file has been deleted. Then it will print an error message and create a new file
    # All previous calculation will be lost if the file has gone
    except FileNotFoundError:
        print("The file has not been found!")
        print("The program will create a new file and save the calculations from this moment on.")
        file = write_file()
    for line in file: #  The file information can be displayed, if the file wasn't there it won't show any calculations
        line = line.replace("\n", "")
        print(line)
    file.close()

#*** Main Program ***
# Most of the main program calls upon functions in a modular approach
# Introduction to calculator
print("\nWelcome to the Simple Calculator.")
# loop to make sure the filename given is in the correct format.
# If it is blank then it will use 'calculations.txt' as a default filename 
while True: 
    filename = get_filename()
    if filename == "":
        filename = "calculations.txt"
        print(f"\nNothing inputted - The filename {filename} will be used!\n")
        break
    filename_length_ok = check_filename_length() # check to see if filename is less than 20 chars
    if filename_length_ok == False:
        continue
    filename_has_no_symbol = check_filename_symbol() # check to see if there are no symbols being used in the filename
    if filename_has_no_symbol == False:
        continue
    filename = (f"{filename}.txt")
    file_exists = check_file_exists() # check to see if the filename already exists, and if so, does the user want to overwrite the file.
    if file_exists == True:
        save_over = input(f"""Do you want to save over the file {filename}? 
All existing data will be lost Y/N: """).upper()
        if save_over == 'Y' or save_over == 'YES':
            print(f"The file {filename} has been overwritten!")
        else:
            print(f"The file {filename} will not be overwritten. Please try again!")
            continue
    print(f"\nThe file name {filename} has been accepted. Thank you.")
    break

# write a new file to capture calculations
file = write_file()
file.write("Saved Calculations\n") # Add this text to the top of every new file so it has a header

# open the file created again to append all the new calaulations into the file.
file = append_file()

# loop the main menu until the correrct option is chosen
while True:
    menu_selection = main_menu() # save the option selected
    # depending on the option selected it will run the required action
    if menu_selection == '1': # this is the calculation option
        print("\nFirst number")
        num1 = number() # get first number
        print("\nSecond number")
        num2 = number() # get second number
        while True: #  loop to choose that the correct menu item has been selected
            select_operation = operation() 
            if select_operation == '1' or select_operation == '2' or select_operation == '3' or select_operation == '4':
                break
            else:
                print("You need to put an answer between \'1 - 4\'. Please try again")
        answer, operator = do_calculation() # run the do_calculation function and return answer and operator variables in that order
        try: # this error handling was needed as if the user had divided by zero it would give a text response (not a number)
            if answer % 1 == 0: # if the number can be divided by zero
                answer = int(answer)
        except Exception: # There could be another error here caused by the text of the divide by zero, so didn't use Valueerror, but Exception instead
            pass # any data is fine in the variable answer, so it would just carry on if it couldn't turn the answer into an integer
        print_calc = (f"{num1} {operator} {num2} = {answer}\n") # saves the written calculation to be displayed on the screen and written to the file
        print(f"\nThe answer to {print_calc}")
        answer_saved_to_file() # save the calculation to the bottom of the file and closes the file

# This menu option will display all calculations from the file. If file not found, it will create a new file
    if menu_selection == '2':
        print() # this was used for formatting to make it read better
        show_file() # run the show file function to display all the contents of the file on screen

# This menu selection exits the program, it doesn't need to save the file as it should be doing that during the program process.
# This will display the text and close
# You can check the file for the saved calculations. However, in the visual code IDE it had a questionmark for the divide sign?
# When viewed on notepad or in the terminal, the divide sign is there.
# Update - This has now been fixed by adding encoding = "utf-8-sig" to all the file open arguments.
    if menu_selection == '0':
        print("Thank you for using the simple calculator")
        print(f"Your calculations will be saved in {filename}.")
        print("\nGoodbye!\n")
        break
    
    # If the wrong menu option was chose,n the program will show not vaild and hint again at what should be inputted
    else:
        print("\nNot a valid slection please type 1, 2, or 0. Thanks.")

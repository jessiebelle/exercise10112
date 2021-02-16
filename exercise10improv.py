import getpass
correct_pin = '1234'
number_of_attempts = 0
supplied_pin = ""
max_attempts = 3
while supplied_pin != correct_pin and number_of_attempts < max_attempts:
    supplied_pin = getpass.getpass("Enter your PIN: ")
    number_of_attempts = number_of_attempts + 1

    if len(supplied_pin) != 4:
        print("Error! 4 numbers required")
    if supplied_pin == correct_pin:
        print("Congratulations, correct pin!")
    else:
        print("Wrong number, please try again")
        print('You have ' + (str(max_attempts - number_of_attempts)) + ' attempts left')
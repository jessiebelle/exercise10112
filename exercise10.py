# pin needs to be only 4 numbers
# needs to be the same as hard - coded
# restrict number of attempts to 3
# output message for success
# output message for failure
import getpass
correct_pin = '1234'
max_tries = 0
supplied_pin = getpass.getpass("Enter your PIN: ")
# if len(supplied_pin) !=4:
#     print("Error! Only 4 numbers allowed ")
# when above happens, we do not need the below error message

while supplied_pin != correct_pin and max_tries <2:
    if len(supplied_pin) != 4:
        print("Error! 4 numbers required")
    print("Wrong number, please try again")
    print('You have ' + (str(2 - max_tries)) + ' attempts left')
    supplied_pin = getpass.getpass("Enter your PIN: ")
    max_tries = max_tries +1
    if max_tries == 2:
        print("Run out of tries!")

if supplied_pin == correct_pin:
    print("Congratulations, correct pin!")


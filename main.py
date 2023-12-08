# making a list to collect the data collected at the end for analysis
data = []
# ask for the person's name
while True:
    name = input("Enter a name: ")
    name = name.capitalize()
    # Check if the input is a non-empty string without numbers
    if name.isalpha() and name.strip():
        break
    else:
        print("Please enter a valid string (no numbers or blank spaces).")

print("You entered a valid name:", name)
# adding name to the data list
data.append(name)
# ask their gender
while True:
    try:
        # we collect data from the user first
        gender = input('Enter Your Gender (M/F): ')
        # then we capitalize it for presentation and further processing
        g = gender.capitalize()
        # this if block checks for correct data has been input
        if g == "M" or g == "F":
            # basic print coz am new
            print("Gender:", g)
            # if the Valid input is captured, we exit the loop
            break
        else:
            # this message will be printed out if the valid input is not captured
            print("Specify with Male (M) or Female (F)")
            # the except block will catch anything freaky
    except Exception as e:
        print(f"An error occurred: {e}")
# adding gender to the list
data.append(g)
# ask their age
while True:
    # this while loop helps in preventing the use of str or float on the code.
    try:
        # data collection
        age = input("Enter Your Age: ")
        # converting to an integer to check if there are numbers or letters used. if it converts to an integer the
        # input will be valid. if there is a value error then it means the data is in text form hence it will be
        # correct.
        int(age)
        print("You are", age, "years old")
        break
    except ValueError:
        print("Please enter valid age, Numbers only")
# adding age to the data list
data.append(age)
# ask marital status
while True:
    try:
        # we collect data from the user first
        status = input('Enter Your Marital Status (Single/Married): ')
        # then we capitalize it for presentation and further processing
        s = status.upper()
        # this if block checks for correct data has been input
        if s == "SINGLE" or s == "MARRIED":
            # basic print coz am new
            print("Marital Status:", s)
            # if the Valid input is captured, we exit the loop
            break
        else:
            # this message will be printed out if the valid input is not captured
            print("Specify with Single or Married")
            # the except block will catch anything freaky
    except Exception as e:
        print(f"An error occurred: {e}")
# adding status to the data list
data.append(s)
# run it through as sorter and send them to the respective groups, data structures
print(data)


# the groups are; sunday school, english women or ushirika, husbands, youth
# sorting function
def sorter():
    # youth
    if int(data[2]) < 15:
        print("You are part of the Sunday School")
    elif int(data[2]) >= 15 > 18:
        print("You are part of the Teens")
    elif int(data[2]) >= 18 and data[3] == 'SINGLE':
        print("You are part of the Youth")
    elif data[1] == 'F' and int(data[2]) >= 18 and data[3] == 'MARRIED':
        print("You can join the English women Group or Ushirika wa Wanawake wa Kristo")
    elif data[1] == 'M' and int(data[2]) >= 18 and data[3] == 'MARRIED':
        print("You can join the Christians Husband Fellowship")


print(sorter())

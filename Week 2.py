# 1.Create a program that asks the user to enter their age and whether or not they have a driver's license. 
# If the user is at least 18 years old and has a driver's license, the output should be as follows
# "You are able to drive : True
# If not, then
# "You are able to drive : False

age=input("Please enter your age: ")
license=input("Do you have a driver's license? (Yes/No): ")
a=int(age)
result = a >= 18 and b == "Yes"
print("You are able to drive: " + str(result))


# 2. (Explore some String functions).
# Create a program that asks the user for a password, and checks if it meets the following criteria:
# at least 8 characters long
# If the password meets all of these criteria, print "Password accepted : True", otherwise print "Password accepted : False".

password = input("Please choose a password that is atleast 8 characters long: " )
password_lenght = str.__len__(password)
result = password_lenght>=8
print("Password accepted: " + str(result))


# 3. Write a program that asks the user to enter two integers and checks if they are both even. 
# If they are, print "Both numbers are even : True", otherwise print "Both numbers are even : False".
# If at least one is even print "At least one number is even : True", else "At least one number is even : False".
# Hint : use modulo operator % here

number1,number2=input("Enter 2 even numbers:").split()
number1=int(number1) % 2
number2=int(number2) % 2
result = (number1 == 0) or (number2 == 0)
print("At least one number is even: " + str(result))


# 4. Write a program that asks the user to enter a year and checks if it is a leap year. 
#A leap year is defined as a year that is divisible by 4 but not by 100, or a year that is divisible by 400. 
#If the year is a leap year, print "Leap year : True", otherwise print "Leap year : False".

Year=input("Enter the year to check if a leap year: ")
Year=int(Year)
result1 = (Year % 4 == 0) and not(Year % 100 == 0)
result2 = Year % 400 == 0
result = result1 or result2
print("Leap year : " +str(result))

# (task with a star, optional) 
# 5.Create the program which asks to enter the date (day, month, year). 
# If the date is valid print : "Date valid : True" else "Date valid : False" 




# 1.  assign a number to a variable between 1 -10
# 2. ask a user to guess a number between 1-10
# 3. cast the number the user gave you to an int
# 3b. (optional) cast the correct number into a str
# 4. If the number is equal to thr correct number then:
# 5. print an awesome message
# 6. if, not Print a sad message
# 7. if the number was within 1, print that they were close.
# 8. add to the message what was the correct number and what
# the number was

# Type code below
#######################################################

correct_number = 4
user_guess = input("Guess a number between 1 and 10: ")
user_guess_int = int(user_guess)
correct_number_str = str(correct_number)
if (user_guess_int == correct_number):
    print("Congratulations! That's correct!")
elif (user_guess_int + 1 == correct_number):
    print("But you were very close! The correct number was " +
          correct_number_str + ".")
elif (user_guess_int - 1 == correct_number):
    print("But you were very close! The correct number was " +
          correct_number_str + ".")
else:
    print("Sorry, that's incorrect. The correct number was " +
          correct_number_str + ".")

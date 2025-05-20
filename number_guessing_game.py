from random import randint

def number_guess():
    
    while True: # For generating new number after the user play again and renewation of attempts
        number = randint(1, 100)
        attempt = 0

        while True:# For continuation of guessing new number
             try:# To fix error if user enter wrong input in guess
                
                 guess = int(input("enter your guess: "))
                 attempt += 1    
         
             except ValueError:
                 print("please enter only number between 1 and 100")
                 continue # To continue the programme if user enters wrong input as guess
         
             if guess == number:
                 print(f"congratulation! your guess is correct in {attempt} attempts😃")# For correct guess
                 
             # scoring system
                 if attempt <= 2:
                     print("Your score is: 100\nExcellent! keep it up😃")
                
                 elif attempt <= 4 and attempt > 2:
                     print("Your score is: 80\nGreat! keep it up🙂")
                 elif attempt <= 6 and attempt > 4:
                     print("Your score is: 60\nNot bad keep it up😌")
                 elif attempt <= 8 and attempt > 6:
                     print("Your score is: 40\nBetter luck next time😔")
                 else:
                     print("Your score is: 20\nNeeds improvement😣")
                     
                 while True:# If user wants to play again
                     play_again = input("Do you want to play again? type('y' for yes and 'n' for no)").strip().lower()
                     if play_again == "y":
                        break # break inner loop if user want to play again
                     elif play_again == "n":
                        print("Thanks for playing")
                        return # break outer loop if user did not want to play again
                     else:
                        print("please type only 'y' or 'n' ")
                 break # To renew the number of attempts after the user play again
# For guessing lower than the number:   
             elif guess < number:
                 print(f"Your guess is lower than number")
# For guessing higher than the number: 
             else:
                 print(f"Your guess is higher than number")
               
number_guess()
     
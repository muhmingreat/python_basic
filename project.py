import random
# Dice game
# while  True:
#     choice = input("Roll the dice ? (y/n)").lower()
#     if  choice  == 'y' :
#         die1 = random.randint(1,6)
#         die2 = random.randint(1,6)
#         print(f'{ die1} {die2}')
#     elif choice == 'n':
#         print('Thanks for Playing')
#         break
#     else :
#         print("You Enter wrong numbery")
# number_to_guess = random.randint(1,100)
# while True:
#     try:
#         guess = int(input("Guess the number from 1 and 100 "))
       
#         if guess < number_to_guess:
#             print("Too Low!")
#         elif guess > number_to_guess:
#             print('Too High')  
#         else:
#             print("Congrate you win")    
#             break 
        
     
#     ercept ValueError:
        # print("Invalid Numer")
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {ROCK:'🥌', SCISSORS:'✂️', PAPER:"📄" }
choices = tuple(emojis.keys())

# while True:
def get_user_choice () :
     while True:   
        user_choice = input('Rock Paper or Scissor (r/p/s)').lower()
        if user_choice  in choices:
            return (user_choice)
        else:
            print('Invalid Choice')
        
def display_choice(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}' ) 
    print(f'Computer chose {emojis[computer_choice]}')  

def determine_winner(user_choice, computer_choice):
   
    if user_choice == computer_choice:
        print('Tie')    
                    
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)):
        print('You win')
    else:
        print('You lose')

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choice(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()

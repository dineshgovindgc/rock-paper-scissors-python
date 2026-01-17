import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice=""
computer=[rock,paper,scissor]
computer_choice=random.choice(computer)
while True:
    print("Let's Play the Game 🎯 \n1 - Rock\n2 - Paper\n3 - Scissor\n4 - Exit")
    user=int(input())
    if user==1:
        user_choice=rock
        print(user_choice)
        print(computer_choice)
        if computer_choice==computer[1]:
            print("Computer Win's 🥲")
        elif computer_choice==computer[2]:
            print("You win the game 🔥")
        else:
            print("Match Draws 😃")
    elif user==2:
        user_choice=paper
        print(user_choice)
        print(computer_choice)
        if computer_choice==computer[2]:
            print("Computer Win's 🥲")
        elif computer_choice==computer[0]:
            print("You win the game 🔥")
        else:
            print("Match Draws 😃")
    elif user==3:
        user_choice=scissor
        print(user_choice)
        print(computer_choice)
        if computer_choice==computer[0]:
            print("Computer Win's 🥲")
        elif computer_choice==computer[1]:
            print("You win the game 🔥")
        else:
            print("Match Draws 😃")
    elif user==4:
        print("Thank you ☺️")
        break
    else:
        print("Enter the valid choice 👺")
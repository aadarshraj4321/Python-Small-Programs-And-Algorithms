

import random

random_float = random.random()
print(random_float)


print(random_float * 12)























import random





def rock():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")




def paper():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")



def scissor():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")




# 1 == Rock
# 2 == Paper
# 3 == Scissor

# Paper Beat Rock
# Scissor Beat paper
# Rock Beat Scissor

def rock_paper_scissor(user_input):
    comp_gen = random.randint(1, 3)
    if (user_input == comp_gen):
        print("Match Tie")

    elif (user_input == 1) and (comp_gen == 2):
        print("Paper Beat Rock. You Are Losser")
        paper()

    elif (user_input == 2) and (comp_gen == 3):
        print("Scissor Beat Paper. You Are Losser")
        scissor()

    elif (user_input == 3) and (comp_gen == 2):
        print("Scissor Beat paper. You Are Winner")
        scissor()

    elif (user_input == 2) and (comp_gen == 1):
        print("Paper Beat Rock. You Are Winner")
        paper()

    elif (user_input == 1) and (comp_gen == 3):
        print("Rock Beat Scissor. You Are Losser")
        scissor()

    elif (user_input == 3) and (comp_gen == 1):
        ("Rock Beat Scissor. You Are Winner")
        scissor()


print("Select     1. Rock     2. Paper     3. Scissor")



print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")




print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")





print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print()

user_input = int(input("Enter Your Number Rock/Paper/Scissor : "))
print()
print(rock_paper_scissor(user_input))




answer = int(input("What do you choose?Type 0 for rock, 1 for paper and 2 for scissors:\n"))
comp_val = random.randint(0,2)
if((comp_val == 0 and answer == 1) or (comp_val == 1 and answer == 2) or (comp_val == 2 and answer == 0)):
    print("You win. Congratss.")
elif((comp_val == 1 and answer == 0) or (comp_val == 2 and answer == 1) or (comp_val == 0 and answer == 2)):
    print("Computer wins and You lose!!")
elif(comp_val == answer):
    print("It's a draw")
else:
    print("That is not a value in the range.")

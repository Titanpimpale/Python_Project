name = input("Hare krishna, Welcome to our game to find Krishna (please enter your name): ")
ans = input(f"Let's start {name}! (yes/no) ").lower()
if ans == "yes":
    ans = input("you have come to juhu beach do you want to go temple or walk to beach (walk/temple)").lower()
    if ans == "temple":
        ans = input("take fruit/flower or walk directly to temple(buy/walk) ").lower()
        if ans == "buy":
            print("yes you wins krsna heart, YOU WIN ")
        elif ans == "walk":
            print("You go to temple and hear kirtan and glories of krsna YOU LIFE IS SUCCESS!")
        else:
            print("Not a valid input")
    elif ans == "walk":
        ans = input("There is stranger Do you want to talk?(yes/no) ").lower()
        if ans == "yes":
            ans =input("Stranger is a devotee he gives you a bhagavat gita do you want it (yes/no) ").lower()
            if ans=="yes":
                print("your life is subline You Get krsna by reading YOU WIN")
            elif ans == "no":
                print("You missed the oppurunity try next time")
        elif ans =="no":
            print("you offened a stranger GAME OVER!")
    else :
        print("Invalid Input")
elif ans =="no":
    print("Chant hare krishna and be happy Game over")

# CTI 110
# P3LAB1 - Choose your own adventure
# Hughes
# 10/22/24

def main():
    print("Choose your own adventure")
    go_home()

def go_home():
    print(" You decide to go home.")
    print("But should you get some food?")
    print("1. Order pizza")
    print("2. Get chinese")
    choice = int(input())
    if choice ==1: 
        get_pizza()
    elif choice ==2: 
        get_chinese()

def get_pizza():
    print("You paiently wait on your door dasher.")

def get_chinese():
    print("All of the nearby resturants are closed, you deside to drive.")

# start the program
main()
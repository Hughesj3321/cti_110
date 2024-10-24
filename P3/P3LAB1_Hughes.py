# CTI 110
# P3LAB1 - Choose your own adventure
# Hughes
# 10/22/24


def main():
    print("Choose your own adventure")
    print("Your friends want to explore a spooky house.")
    print("1. Go with friends.")
    print("2. Go home.")
    choice = int(input())
    if choice ==1:
        go_with_friends()
    elif choice ==2:
        go_home()

def go_with_friends():
    print("You rock, paper, siccors who goes to the door.")
    print("1. Rock")
    print("2. Paper")
    print("3. Siccors")
    choice = int(input())
    if choice ==1:
        print("John goes to the door...he dies.")
    if choice ==2:
        print("Chris goes to the door...he hears someone inside.")
    if choice ==3:
        print("You go to the door and you sence that someone is watching you.")

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
    print("While waiting on the arival of your less than stellar door dasher, you get a phone call from a unknown number.")
    print("You look at the phone as it rings while thinking,'I hate robo calls,'")
    print("The caller leaves a voicemail, it's Chris.")
    print("You call Chris.")
    print("1. Ask Chris about the new number.")
    print("2. Ask Chrs about the house.")
    choice = int(input())
    if choice ==1:
        ask_about_number()
    elif choice==2:
        ask_about_house()

def ask_about_number():
    print("Your door dasher has arrived.")
def ask_about_house():
    print("Someone knocks at the door.")
def get_chinese():
    print("All of the nearby resturants are closed, you deside to drive.")

# start the program
main()
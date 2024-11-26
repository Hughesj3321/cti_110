import random
import time
import sys

class ExtendedHorrorGame:
    def __init__(self):
        self.player_name = ""
        self.survived = False
        self.killer_identity = ""
        self.weapon = None
        self.allies = []
        self.injuries = 0
        self.knowledge_points = 0
        self.final_outcome = ""

    def slow_print(self, text, delay=0.03):
        """Print text with a typewriter effect."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def intro(self):
        print("\n🔪🩸 SURVIVE THE NIGHT 🩸🔪")
        print("A terrifying game of cat and mouse begins...")
        time.sleep(1)
        
        self.player_name = input("\nWhat is your name? ").strip()
        
        self.slow_print(f"\nWelcome, {self.player_name}. Your choices will determine whether you live or die tonight...")
        time.sleep(1)
        
        print("\nYou're a high school student home alone on a stormy night.")
        print("Strange things have been happening in your small town recently...")

    def initial_setup(self):
        print("\nBefore the night begins, choose your background:")
        print("1. Athlete with good physical skills")
        print("2. Tech-savvy student with access to security systems")
        print("3. Drama club member skilled in deception")
        
        background_choice = input("Select your character type (1/2/3): ")
        
        if background_choice == '1':
            self.weapon = "sports trophy"
            self.knowledge_points += 2
        elif background_choice == '2':
            self.weapon = "socket wrench"
            self.knowledge_points += 3
        else:
            self.weapon = "prop knife from drama club"
            self.knowledge_points += 1
        
        return self.first_encounter()

    def first_encounter(self):
        print("\nSuddenly, the power goes out. You hear a noise downstairs...")
        print("1. Grab your phone and call a friend")
        print("2. Quietly investigate the noise")
        print("3. Barricade yourself in your room")
        
        choice = input("What do you do? (1/2/3): ")
        
        if choice == '1':
            self.allies.append("best friend")
            return self.friend_help_route()
        elif choice == '2':
            return self.investigation_route()
        else:
            return self.barricade_route()

    def friend_help_route(self):
        print("\nYour friend agrees to stay on the phone and help you...")
        time.sleep(1)
        
        print("Suddenly, you hear a crash downstairs!")
        print("1. Ask your friend to call the police")
        print("2. Tell your friend to stay quiet")
        print("3. Ask your friend to track your phone's location")
        
        choice = input("What's your next move? (1/2/3): ")
        
        if choice == '1':
            self.knowledge_points += 1
            self.allies.append("local police")
            return self.police_intervention()
        elif choice == '2':
            return self.quiet_survival_route()
        else:
            self.knowledge_points += 2
            return self.tracking_route()

    def quiet_survival_route(self):
        """Handle the route where the player tries to stay quiet"""
        print("\nYou whisper to your friend to stay completely silent...")
        time.sleep(1)
        
        print("Footsteps creep closer to your location...")
        print("1. Hold your breath")
        print("2. Prepare to fight if discovered")
        print("3. Try to move to a hidden spot")
        
        choice = input("What do you do? (1/2/3): ")
        
        if choice == '1':
            self.knowledge_points += 2
        elif choice == '2':
            self.weapon = "nearby lamp"
            self.injuries += 1
        else:
            self.knowledge_points += 1
        
        return self.killer_confrontation()

    def tracking_route(self):
        """Handle the route where your friend tracks your phone"""
        print("\nYour friend begins tracking your phone location...")
        time.sleep(1)
        
        print("They realize the killer might be closing in!")
        print("1. Try to create a distraction")
        print("2. Prepare an ambush")
        print("3. Look for an escape route")
        
        choice = input("What's your strategy? (1/2/3): ")
        
        if choice == '1':
            self.knowledge_points += 1
        elif choice == '2':
            self.weapon = "heavy object"
            self.knowledge_points += 2
        else:
            return self.escape_attempt()
        
        return self.killer_confrontation()

    def investigation_route(self):
        possible_locations = ["kitchen", "basement", "living room"]
        danger_location = random.choice(possible_locations)
        
        print(f"\nYou slowly move towards the {danger_location}...")
        time.sleep(1)
        
        print("You find signs of a break-in!")
        print("1. Look for a better weapon")
        print("2. Set up a trap")
        print("3. Try to escape through a window")
        
        choice = input("What do you do? (1/2/3): ")
        
        if choice == '1':
            self.weapon = "kitchen knife"
            self.knowledge_points += 1
        elif choice == '2':
            self.knowledge_points += 2
        else:
            return self.escape_attempt()
        
        return self.killer_confrontation()

    def escape_attempt(self):
        """Handle escape route scenarios"""
        print("\nYou attempt to escape the killer...")
        time.sleep(1)
        
        print("The escape is risky and unpredictable!")
        print("1. Sneak out quietly")
        print("2. Create a loud diversion")
        print("3. Hide and wait for the right moment")
        
        choice = input("How will you try to escape? (1/2/3): ")
        
        if choice == '1':
            self.knowledge_points += 2
        elif choice == '2':
            self.injuries += 1
        else:
            self.knowledge_points += 1
        
        return self.killer_confrontation()

    def barricade_route(self):
        print("\nYou've locked the door and pushed furniture against it...")
        time.sleep(1)
        
        print("You hear scratching and whispers outside...")
        print("1. Stay absolutely silent")
        print("2. Try to communicate with the intruder")
        print("3. Look for an alternative escape route")
        
        choice = input("What's your strategy? (1/2/3): ")
        
        if choice == '1':
            self.knowledge_points += 2
        elif choice == '2':
            self.injuries += 1
        else:
            return self.escape_attempt()
        
        return self.killer_confrontation()

    def police_intervention(self):
        print("\nThe police are on their way, but the killer knows...")
        time.sleep(1)
        
        print("The killer seems prepared for their arrival.")
        print("1. Set up an ambush")
        print("2. Create a distraction")
        print("3. Prepare to fight")
        
        choice = input("How will you use the police's arrival? (1/2/3): ")
        
        if choice == '1':
            self.knowledge_points += 3
        elif choice == '2':
            self.knowledge_points += 1
        else:
            self.injuries += 1
        
        return self.killer_confrontation()

    def killer_confrontation(self):
        killer_options = [
            "Vengeful Ex-Student",
            "Local Serial Killer",
            "Family Revenge Seeker",
            "Psychopathic Classmate",
            "Unknown Stalker"
        ]
        
        self.killer_identity = random.choice(killer_options)
        
        print(f"\nThe killer reveals themselves: {self.killer_identity}!")
        print("Final confrontation begins...")
        
        survival_factors = self.knowledge_points - self.injuries
        survival_chance = max(0.1, min(0.9, 0.5 + (survival_factors * 0.1)))
        
        self.survived = random.random() < survival_chance
        
        return self.determine_ending()

    def determine_ending(self):
        endings = {
            (True, "Heroic"): "You outsmarted the killer and saved yourself and others!",
            (True, "Survivor"): "You barely escaped with your life, wounded but alive.",
            (True, "Lucky"): "By sheer luck and quick thinking, you survived the night.",
            (False, "Tragic"): "The killer's revenge was complete. Your story ends here.",
            (False, "Close Call"): "You fought bravely but ultimately fell to the killer.",
            (False, "Unexpected"): "A twist of fate sealed your unfortunate destiny."
        }
        
        ending_type = "Heroic" if self.survived and self.knowledge_points > 4 else \
                      "Survivor" if self.survived else \
                      "Tragic" if self.injuries > 2 else \
                      "Close Call"
        
        self.final_outcome = endings.get((self.survived, ending_type), 
                                         "An unpredictable and mysterious end...")
        
        return self.game_conclusion()

    def game_conclusion(self):
        print("\n--- GAME OVER ---")
        print(f"Player: {self.player_name}")
        print(f"Killer: {self.killer_identity}")
        print(f"Weapon: {self.weapon}")
        print(f"Allies: {', '.join(self.allies) if self.allies else 'None'}")
        print(f"\n{self.final_outcome}")
        
        print("\nWould you like to play again?")
        replay = input("Enter 'yes' to restart or any other key to exit: ").lower()
        return replay == 'yes'

    def play(self):
        while True:
            self.reset_game()
            self.intro()
            continue_game = self.initial_setup()
            if not continue_game:
                break
            print("\nThanks for playing 'Survive the Night'!")

    def reset_game(self):
        """Reset all game variables for a new playthrough."""
        self.player_name = ""
        self.survived = False
        self.killer_identity = ""
        self.weapon = None
        self.allies = []
        self.injuries = 0
        self.knowledge_points = 0
        self.final_outcome = ""

if __name__ == "__main__":
    game = ExtendedHorrorGame()
    game.play()

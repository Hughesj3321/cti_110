import random
import time
import sys

class GothamSurvivalHorror:
    def __init__(self):
        # Game state variables
        self.player_name = ""
        self.player_background = ""
        self.survived = False
        self.killer_identity = ""
        self.weapon = None
        
        # Character interaction tracking
        self.allies = []
        self.enemies = []
        self.known_locations = []
        
        # Progression metrics
        self.injuries = 0
        self.knowledge_points = 0
        self.fear_level = 0
        self.reputation = 50  # Neutral starting reputation
        
        # Gotham-specific variables
        self.district = ""
        self.current_time = "night"
        self.weather = ""
        
        # Story progression
        self.plot_stages = {
            "introduction": False,
            "first_encounter": False,
            "midpoint_twist": False,
            "final_confrontation": False
        }
        
        # Gotham characters
        self.gotham_characters = {
            "allies": [
                "Commissioner Gordon",
                "Alfred Pennyworth",
                "Lucius Fox",
                "Black Canary",
                "Batwoman"
            ],
            "potential_killers": [
                "Joker's Apprentice",
                "Scarecrow's Experiment",
                "Riddler's Test Subject",
                "Penguin's Revenge Seeker",
                "Two-Face's Vengeful Associate",
                "Mad Hatter's Mind-Controlled Killer"
            ],
            "neutral_npcs": [
                "Corrupt GCPD Officer",
                "Underground Information Broker",
                "Arkham Asylum Psychiatrist",
                "Desperate Gotham Citizen"
            ]
        }
        
        # Detailed locations
        self.gotham_locations = [
            "Crime Alley",
            "Arkham Asylum Exterior",
            "Abandoned Wayne Enterprises Warehouse",
            "Gotham Central Station",
            "Gotham City Docks",
            "Underground Subway Tunnel",
            "Abandoned Pharmaceutical Lab",
            "Gothic Cathedral in Downtown Gotham"
        ]

    def slow_print(self, text, delay=0.03):
        """Print text with a dramatic typewriter effect."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def set_initial_context(self):
        """Establish the initial game setting and context."""
        # Set random weather and district
        self.weather = random.choice(["Heavy Rain", "Thick Fog", "Electrical Storm", "Freezing Night"])
        self.district = random.choice(self.gotham_locations)
        
        print(f"\n🦇 GOTHAM SURVIVAL: {self.weather.upper()} 🌆")
        self.slow_print(f"Location: {self.district}")
        time.sleep(1)

    def character_selection(self):
        """Allow player to choose their background and starting attributes."""
        print("\nChoose your background in Gotham:")
        backgrounds = [
            "Gotham City Journalist",
            "GCPD Junior Detective",
            "Wayne Enterprises Junior Researcher",
            "Arkham Asylum Medical Intern",
            "Underground Resistance Member"
        ]

        for i, bg in enumerate(backgrounds, 1):
            print(f"{i}. {bg}")

        choice = int(input("\nSelect your background (1-5): "))
        self.player_background = backgrounds[choice - 1]
        
        # Assign initial attributes based on background
        background_attributes = {
            "Gotham City Journalist": {
                "starting_weapon": "Camera with Flash",
                "knowledge_bonus": 2,
                "allies_bonus": ["Underground Informant"]
            },
            "GCPD Junior Detective": {
                "starting_weapon": "Service Revolver",
                "knowledge_bonus": 3,
                "allies_bonus": ["Commissioner Gordon"]
            },
            "Wayne Enterprises Junior Researcher": {
                "starting_weapon": "High-Tech Flashlight",
                "knowledge_bonus": 2,
                "allies_bonus": ["Lucius Fox"]
            },
            "Arkham Asylum Medical Intern": {
                "starting_weapon": "Medical Syringe",
                "knowledge_bonus": 1,
                "allies_bonus": ["Sympathetic Nurse"]
            },
            "Underground Resistance Member": {
                "starting_weapon": "Makeshift Shiv",
                "knowledge_bonus": 2,
                "allies_bonus": ["Resistance Contact"]
            }
        }

        selected_attributes = background_attributes[self.player_background]
        self.weapon = selected_attributes["starting_weapon"]
        self.knowledge_points += selected_attributes["knowledge_bonus"]
        self.allies.extend(selected_attributes["allies_bonus"])

    def initial_encounter(self):
        """First major story encounter with multiple narrative branches."""
        print(f"\nAs a {self.player_background}, you find yourself in {self.district}...")
        
        encounter_scenarios = [
            "Witnessing a Mysterious Murder",
            "Intercepting a Cryptic Message",
            "Stumbling Upon a Sinister Experiment",
            "Being Targeted by an Unknown Killer"
        ]
        
        scenario = random.choice(encounter_scenarios)
        print(f"Scenario: {scenario}")
        
        # Implement branching narrative based on scenario
        # This is a simplified version - you'd expand this with more complex interactions
        print("\nWhat do you do?")
        print("1. Investigate Immediately")
        print("2. Call for Backup")
        print("3. Try to Escape")
        
        choice = input("Select your action (1-3): ")
        
        if choice == '1':
            self.knowledge_points += 2
            self.fear_level += 1
        elif choice == '2':
            self.allies.append(random.choice(self.gotham_characters["allies"]))
            self.reputation += 10
        else:
            self.fear_level += 2
            self.injuries += 1

    def play(self):
        """Main game loop with multiple stages of gameplay."""
        self.set_initial_context()
        self.character_selection()
        self.initial_encounter()
        
        # Additional stages would be added here
        # For now, this is a simplified version
        print("\nGame is still in development. More stages coming soon!")

    def reset_game(self):
        """Reset all game variables for a new playthrough."""
        # Similar to previous implementation, reset all attributes
        pass

if __name__ == "__main__":
    game = GothamSurvivalHorror()
    game.play()

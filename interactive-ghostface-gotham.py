import random
import time
from enum import Enum, auto

class GameState(Enum):
    INTRODUCTION = auto()
    INVESTIGATION = auto()
    PURSUIT = auto()
    CONFRONTATION = auto()
    ENDGAME = auto()

class Player:
    def __init__(self):
        self.evidence = []
        self.reputation = 50  # Neutral starting point
        self.detective_skill = random.randint(3, 8)
        self.health = 100

class Ghostface:
    def __init__(self):
        self.locations_stalked = []
        self.victims_count = 0
        self.complexity = random.uniform(0.5, 0.9)

class GothamAdventure:
    def __init__(self):
        self.player = Player()
        self.ghostface = Ghostface()
        self.game_state = GameState.INTRODUCTION
        self.current_location = "Gotham City"

    def narrative_print(self, text, delay=0.03):
        """Print text with dramatic typing effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print("\n")

    def clear_screen(self):
        """Simulate clearing screen"""
        print("\n" * 50)

    def introduction(self):
        """Game introduction sequence"""
        self.clear_screen()
        self.narrative_print("The night is thick with tension in Gotham City...")
        self.narrative_print("A series of brutal murders have the city on edge.")
        self.narrative_print("As Batman, you must uncover the identity of the mysterious Ghostface killer.")
        
        input("\nPress Enter to begin the investigation...")
        self.game_state = GameState.INVESTIGATION

    def investigation_menu(self):
        """Interactive investigation options"""
        while True:
            self.clear_screen()
            self.narrative_print(f"Current Location: {self.current_location}")
            self.narrative_print(f"Evidence Collected: {len(self.player.evidence)}")
            
            print("Investigation Options:")
            print("1. Forensic Analysis")
            print("2. Street Informant")
            print("3. Crime Scene Search")
            print("4. Bat-Computer Analysis")
            print("5. Continue Pursuit")
            
            choice = input("\nChoose your investigation method (1-5): ")
            
            if choice == "1":
                self.forensic_investigation()
            elif choice == "2":
                self.street_intelligence()
            elif choice == "3":
                self.crime_scene_search()
            elif choice == "4":
                self.bat_computer_analysis()
            elif choice == "5":
                if len(self.player.evidence) >= 3:
                    self.game_state = GameState.PURSUIT
                    return
                else:
                    self.narrative_print("You need more evidence before pursuing Ghostface!")
            else:
                self.narrative_print("Invalid choice. Try again.")

    def forensic_investigation(self):
        """Forensic investigation method"""
        forensic_clues = [
            "Unique DNA trace",
            "Partial fingerprint",
            "Rare knife manufacturing stamp",
            "Encrypted digital fragment"
        ]
        clue = random.choice(forensic_clues)
        self.player.evidence.append(clue)
        self.narrative_print(f"Forensic Breakthrough: {clue}")
        input("\nPress Enter to continue...")

    def street_intelligence(self):
        """Gather street-level information"""
        intel_options = [
            "Rumor of a vendetta against city officials",
            "Underground whispers about a serial killer",
            "Mysterious financial transactions",
            "Connection to unsolved cold cases"
        ]
        intel = random.choice(intel_options)
        self.player.evidence.append(intel)
        self.narrative_print(f"Street Informant Reveals: {intel}")
        input("\nPress Enter to continue...")

    def crime_scene_search(self):
        """Detailed crime scene investigation"""
        scene_clues = [
            "Cryptic message left behind",
            "Unusual trace evidence",
            "Psychological profile hint",
            "Potential killer's escape route"
        ]
        clue = random.choice(scene_clues)
        self.player.evidence.append(clue)
        self.narrative_print(f"Crime Scene Discovery: {clue}")
        input("\nPress Enter to continue...")

    def bat_computer_analysis(self):
        """Advanced digital investigation"""
        digital_clues = [
            "Network of suspicious connections",
            "Predictive crime pattern",
            "Historical data correlation",
            "Encrypted communication intercept"
        ]
        clue = random.choice(digital_clues)
        self.player.evidence.append(clue)
        self.narrative_print(f"Bat-Computer Analysis: {clue}")
        input("\nPress Enter to continue...")

    def pursuit_phase(self):
        """Interactive pursuit of Ghostface"""
        pursuit_locations = [
            "Abandoned Arkham Asylum",
            "Gotham Central Bridge",
            "Dark Alleyways",
            "Abandoned Steel Mill"
        ]
        
        while self.game_state == GameState.PURSUIT:
            self.clear_screen()
            self.narrative_print("Pursuit Phase: Track down Ghostface")
            
            print("Potential Locations:")
            for i, location in enumerate(pursuit_locations, 1):
                print(f"{i}. {location}")
            print("0. Return to Investigation")
            
            choice = input("\nChoose a location to investigate: ")
            
            try:
                choice = int(choice)
                if choice == 0:
                    self.game_state = GameState.INVESTIGATION
                    return
                elif 1 <= choice <= len(pursuit_locations):
                    location = pursuit_locations[choice-1]
                    self.current_location = location
                    result = self.pursue_ghostface(location)
                    
                    if result == "confrontation":
                        self.game_state = GameState.CONFRONTATION
                        return
                else:
                    self.narrative_print("Invalid location. Try again.")
            except ValueError:
                self.narrative_print("Please enter a valid number.")

    def pursue_ghostface(self, location):
        """Determine outcome of pursuit in a specific location"""
        pursuit_outcomes = [
            "close_call",
            "evidence_found",
            "confrontation",
            "missed_opportunity"
        ]
        outcome = random.choice(pursuit_outcomes)
        
        if outcome == "confrontation":
            self.narrative_print(f"Confrontation detected at {location}!")
            return "confrontation"
        
        result_messages = {
            "close_call": f"Ghostface narrowly escapes in {location}. Another clue slips away.",
            "evidence_found": f"A crucial piece of evidence discovered in {location}.",
            "missed_opportunity": f"The trail goes cold in {location}. Ghostface remains one step ahead."
        }
        
        self.narrative_print(result_messages[outcome])
        input("\nPress Enter to continue...")
        return outcome

    def confrontation(self):
        """Final confrontation with multiple outcomes"""
        confrontation_locations = [
            "Gotham Central Tower",
            "Abandoned Chemical Plant",
            "Underground Subway Tunnel",
            "Rooftop Showdown"
        ]
        
        location = random.choice(confrontation_locations)
        self.narrative_print(f"FINAL CONFRONTATION AT {location.upper()}!")
        
        # Multiple potential outcomes
        outcomes = [
            "Batman defeats Ghostface, uncovering a deep conspiracy",
            "A narrow escape leaves more questions than answers",
            "A pyrrhic victory with significant personal cost",
            "An unexpected alliance reveals a shocking truth",
            "A psychological battle that challenges Batman's resolve"
        ]
        
        final_outcome = random.choice(outcomes)
        self.narrative_print("\n--- GOTHAM'S FATE ---")
        self.narrative_print(final_outcome)
        
        self.game_state = GameState.ENDGAME

    def play(self):
        """Main game loop"""
        self.introduction()
        
        while self.game_state != GameState.ENDGAME:
            if self.game_state == GameState.INVESTIGATION:
                self.investigation_menu()
            elif self.game_state == GameState.PURSUIT:
                self.pursuit_phase()
            elif self.game_state == GameState.CONFRONTATION:
                self.confrontation()
        
        print("\nThanks for playing Batman vs Ghostface!")

def main():
    random.seed()
    game = GothamAdventure()
    game.play()

if __name__ == "__main__":
    main()

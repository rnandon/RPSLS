from player import Player
import random


class Ai(Player):
    
    # get random gesture for AI player
    def select_gesture(self):
        random_gesture_selector = random.randint(0, len(self.gestures) - 1) # get rand int for range of gestures list - set as current gesture
        selected_gesture = self.gestures[random_gesture_selector]
        self.set_gesture(selected_gesture)
        
        print(selected_gesture)
        print(self.current_gesture)
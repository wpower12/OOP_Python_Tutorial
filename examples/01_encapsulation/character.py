##
# character.py
##

class Character:

    def __init__(self, p_name, p_class, max_health):
        self.player_name  = p_name
        self.player_class = p_class 
        self.max_hp       = max_health
        self.current_hp   = max_health

    def whoAreYou(self):
        print("I am {}, a {}".format(self.player_name, self.player_class))

    def hurt(self, dmg):
        self.current_hp -= dmg

        if self.current_hp <= 0:
            print("I'm dead!")
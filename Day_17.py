# zigzag function

import time, sys
'''

indent = 0
indentIncrease = True

try:
    while True:
        print(' ' * indent, end='')
        print('Muhib_Ullah')
        time.sleep(0.1)

        if indentIncrease:
            indent = indent + 1
            if indent == 20:
                indentIncrease = False
        else: 
            indent = indent - 1
            if indent == 0:
                indentIncrease = True
except KeyboardInterrupt:
    sys.exit()



'''
'''
import sys, time

space = 0
spaceIncrease = True 

try: 
    while True:
        print('  ' * space, end='')
        print('Sardar_sab')
        time.sleep(0.1)
    
        if spaceIncrease:
            space = space + 1
            if space == 20:
                spaceIncrease = False
        else:
            space = space - 1
            if space == 0:
                spaceIncrease = True
except KeyboardInterrupt:
    sys.exit()



'''
class Player():
    def __init__(self, name, points=0, health=100, location= (0, 0)):
        self.name = name
        self.points = points
        self.health = health  
        self.location = location

    def location_move(self, x, y):

        self.location = (x, y)
        print(f"{self.name} moved to ({x}, {y}).")
    
    def gain_points(self, amount):
        self.points += amount
        print(f"{self.name} has gained {amount} points. Total point: {self.points}")

    def take_damage(self, damage):
        if self.health <= 0:
            print(f"{self.name} has been defeated.")
        else:
            print(f"{self.name} took {damage}. health remaining: {self.health}")
    
    def __str__(self):
        return f"Player: {self.name}, Points: {self.points}, Health: {self.health}, Location: {self.location}"
    
if __name__ == "__main__":


    



player = Player("alex", 8, 2, "Pochenki" )
print(show(player))














import random


class Pet(object):

    pets = ['dog', 'cat', 'snake', 'elephant']
    colour = ['green', 'blue', 'red']

    def __init__(self):
        pass

    def get_pet(self):
        pet = random.choice(self.pets)
        colour = random.choice(self.colour)
        return {pet: colour}









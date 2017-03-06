import random


class Pet(object):

    pets = ['dog', 'cat']

    def __init__(self):
        pass

    def get_pet(self):
        return random.choice(self.pets)









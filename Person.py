from Pet import Pet


class Person(object):

    age = None
    pet = None


    def __init__(self, age):
        self.age = age

    def choose_pet(self):
        pet = Pet()
        self.pet = pet.get_pet()




from Person import Person

class Main(object):

    def __main__(self):
        person = Person(25)
        person.choose_pet()
        print(person.pet)
        print(person.age)


if __name__ == '__main__':
    Main().__main__()
__author__ = 'Pedro'
# g's proramming challenge #00 - Random Name Generator
# NOT WORKING - RETURNING MEMORY OBJECT INSTEAD OF NAME
from random import randint

firstname_male = ['Ze','Marcos','Joao','Pedro','Felipe']
lastname_male = [' da Silva',' Nogueira','Figueiredo',' Camargo']


class NameGen():
    def generateName(self):
        generatedname = firstname_male[randint(0,len(firstname_male) - 1)] + lastname_male[randint(0,len(lastname_male) - 1)]
        return generatedname


randname = NameGen()
randname.generateName()
print (randname)

print('test')
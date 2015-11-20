__author__ = 'Pedro'
# g's proramming challenge #00 - Random Name Generator
# NOT WORKING - RETURNING MEMORY OBJECT INSTEAD OF NAME

from random import randrange

firstname_male = ['Ze','Marcos','Joao','Pedro','Felipe','Jacques','Marquito']
lastname_male = ['da Silva','Nogueira','Figueiredo','Camargo']


class NameGen():
    def generateName(self):
        randomindex1 = randrange(0, len(firstname_male))
        randomindex2 = randrange(0, len(lastname_male))
        generatedname = str(firstname_male[randomindex1] +  ' ' + lastname_male[randomindex2])
        print (generatedname)
        return generatedname

while True:
    print ('\n Gerador de Nomes Aleatorios 0.1 \n O nome gerado foi : ')
    newname = NameGen()
    newname.generateName()
    op = str(input('Deseja gerar outro nome ? s/n '))
    if op == 's':
        pass
    if op == 'n':
        print('Processo Finalizado')
        break



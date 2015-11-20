__author__ = 'Pedro'

class AgeinSec():

    def ageToSeconds(self, age):
        months = 12
        days = 30
        hours = 24
        minutes = 60
        seconds = 60
        newage = (age * months * days * hours * minutes * seconds)
        print ('Voce viveu : ' + str(newage) + ' segundos ate o momento')
        return newage

pessoa = AgeinSec()
idade = int(input('Digite a sua idade para ver quantos segundos voce tem de vida'))
pessoa.ageToSeconds(idade)
__author__ = 'Pedro'
# g's programming challenges #02 - Temperature Converter

class TempConv():
    def conversor(self,op,temp):
        if op == 1:
            tempC = (temp - 32) * 5/9
            print ('\n Sua Temperatura em Celsius e: ' + str(tempC) + ' graus')
            return tempC
        if op == 2:
            tempFh = (temp * 9/5) + 32
            print ('\n Sua Temperatura em Farenheit e: ' + str(tempFh)+ ' graus' )
            return tempFh
        else:
            return ('Opcao Invalida')

print ('Opcoes : \n 1 - Celsius para Farenheit\n 2 - Farenheit para Celsius')
op = int(input('Digite a sua Opcao'))
if op > 2:
    print ('opcao invalida')
else:
    temp = int(input('Digite a temperatura desejada'))

newTemp = TempConv()
newTemp.conversor(op,temp)
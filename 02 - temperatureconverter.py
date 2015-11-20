__author__ = 'Pedro'
# g's programming challenges #02 - Temperature Converter

class TempConv():
    def conversor(self,op,temp):
        print ('1 - Fh para Celsius /n 2 - Celsius para Fh')
        if op == 1:
            tempC = (temp - 32) * 5/9
            print ('\n Sua Temperatura em Celsius e: ' + str(tempC) + ' graus')
            return tempC
        if op == 2:
            tempFh = (temp * 9/5) + 32
            print ('\n Sua Temperatura em Farenheit e: ' + str(tempFh)+ ' graus' )
            return tempFh

newTemp = TempConv()
newTemp.conversor(1,44)
import datetime

'''
The Dog Class with Overloaded Addition
'''

class Dog:
    def __init__(self, name, day, month, year, speakText):
        self.name = name        
        self.birth = datetime.date(year, month, day)
        self.speakText = speakText
    
    def speak(self):
        return 'Sonido: {}'.format(self.speakText) 

    def getName(self):
        return 'Nombre: {} '.format( self.name)

    def birthDate(self):
        return  'Fecha de nacimiento: {}'.format(str(self.birth)) 
    
    def changeBark(self, bark):
        self.speakText = bark

    '''
    overload de operador suma 
    '''
    def __add__(self, otherDog): 
        return Dog("Puppy of " + self.name + " and " + otherDog.name, 
                self.birth.day,
                self.birth.month,
                self.birth.year+1,
                self.speakText + otherDog.speakText  )                

    ''' 
    overload del operador equal
    '''
    def __eq__(self, otherDog):
        return self.name == otherDog.name

    def repr(self):
        return self.__repr__

def main():
    boydog = Dog("Fido", 15,5,2004, "WOOF")
    girldog = Dog("Fido", 15,5,2004, "barkbark")
    print(boydog.getName())
    print(girldog.getName())
    print(boydog.speak())
    print(girldog.speak())
    print(boydog.birthDate())
    print(girldog.birthDate())
    boydog.changeBark('woofy')
    print(boydog.speak())

    # crear y modificar datos de objeto
    puppy = boydog + girldog
    print(puppy.speak())
    print(puppy.getName())
    print(puppy.birthDate())

    print(boydog.repr()) # representacion del objeto en memoria

    print('¿Son iguales los perritos?: {}'.format( 'Si' if boydog == girldog else 'No') )

if __name__ == "__main__":
    main()


    
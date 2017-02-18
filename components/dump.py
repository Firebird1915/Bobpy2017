import wpilib

class Dump():

    doubleS = wpilib.DoubleSolenoid

    def __init__(self):
        pass

    def toggle(self):
        #Toggles between foreward and reverse
        if doubleS.get() == 1:
            doubleS.set(2) #Reverse
        else:
            doubleS.set(1) #Forward

    def turnOff(self):
        #Turns it off
        doubleS.set(0)

    def execute(self):
        pass

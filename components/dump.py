import wpilib

class Dump():
    doubleS = wpilib.DoubleSolenoid

    def __init__(self):
        pass
    def toggle(self):
        if doubleS.get() == 1:
            doubleS.set(2) #reverse
        else:
            doubleS.set(1) #Forward

    def turnOff(self):
        doubleS.set(0)

    def dumper(self):
        self.doubleS.set(2)

    def loader(self):
        self.doubleS.set(1)

    def execute(self):
        pass

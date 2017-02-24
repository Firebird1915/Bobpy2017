import wpilib
import logging

class Dump():
    doubleS = wpilib.DoubleSolenoid
    doubleS2 = wpilib.DoubleSolenoid
    pistonToggle = False

    def __init__(self):
        pass

    #Works, but i you hold for too long it triggers multiple times
    #probably should fix that
    def toggle(self):
        if int(self.doubleS.get()) == 1:
            self.dumper()
        else:
            self.loader()


    def turnOff(self):
        doubleS.set(0)
        doubleS2.set(0)

    def dumper(self):
        self.doubleS.set(2)
        self.doubleS2.set(2)

    def loader(self):
        self.doubleS.set(1)
        self.doubleS2.set(1)

    def execute(self):
        pass

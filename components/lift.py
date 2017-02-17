import wpilib
import ctre

class Lift:

    lift_motor = ctre.CANTalon

    def __init__ (self):
         pass

    def goUp(self, amount):
        self.lift_motor.set(amount)

    def execute(self):
        pass

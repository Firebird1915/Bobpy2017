import wpilib
import ctre
from magicbot import MagicRobot

'''
    Magic bot implimentation test
    Things (obviously) are subject to change

    1/13: Because this is a test components are made simply for understanding
    but do nothing.
'''

#Highlevel components before lowlevel components

#lowlevel components
from components.drive import Drive

VOLT_RAMPUP = 24/0.6

class Bob(MagicRobot):

    drive = Drive

    def createObjects(self):
        #Motors and such are set here
        self.rf_motor = rf_motor = ctre.CANTalon(5)
        self.rr_motor = rr_motor = ctre.CANTalon(1)
        self.lf_motor = lf_motor = ctre.CANTalon(3)
        self.lr_motor = lr_motor = ctre.CANTalon(4)

        self.robotDrive = wpilib.RobotDrive(rf_motor,
                                            rr_motor,
                                            lf_motor,
                                            lr_motor)

        rf_motor.setVoltageRampRate(VOLT_RAMPUP)
        rr_motor.setVoltageRampRate(VOLT_RAMPUP)
        lf_motor.setVoltageRampRate(VOLT_RAMPUP)
        lr_motor.setVoltageRampRate(VOLT_RAMPUP)

        rr_motor.reverseOutput(True)
        rf_motor.reverseOutput(True)

        self.stick = wpilib.Joystick(1)


    def teleopPeriodic(self):

        '''Called on each iteration of the control loop'''

        self.robotDrive.setSafetyEnabled(True)
      



                    # The robot does not have a gyro (yet) therefore the input is zero
        self.robotDrive.mecanumDrive_Cartesian(self.stick.getX() / 0.5,
                                               self.stick.getY() / 0.5,
                                               self.stick.getZ() / 0.5 ,0);



if __name__=='__main__':
    wpilib.run(Bob)

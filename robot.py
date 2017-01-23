import wpilib
import ctre
import logging
from networktables import NetworkTable
from magicbot import MagicRobot
from robotpy_ext.common_drivers import navx

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

        #This lets you spit stuff to the dashboard
        self.sd = wpilib.SmartDashboard

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
        lr_motor.reverseOutput(True)
        lf_motor.reverseOutput(True)

        self.stick = wpilib.Joystick(1)

        self.navX = navx.AHRS.create_spi()


    def teleopInit(self):
        self.navX.reset()

    def teleopPeriodic(self):

        '''Called on each iteration of the control loop'''



        self.robotDrive.setSafetyEnabled(True)






        wpilib.Timer.delay(0.10)




        self.drive.move(self.stick.getRawAxis(0),
                        self.stick.getRawAxis(3),
                        -self.stick.getRawAxis(1),
                        self.navX.getAngle())

        wpilib.Timer.delay (0.005) #wait for the motor to update



if __name__=='__main__':
    wpilib.run(Bob)

import wpilib
import ctre
from magicbot import MagicRobot
from robotpy_ext.common_drivers.navx import AHRS

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

        # rf_motor.setVoltageRampRate(VOLT_RAMPUP)
        # rr_motor.setVoltageRampRate(VOLT_RAMPUP)
        # lf_motor.setVoltageRampRate(VOLT_RAMPUP)
        # lr_motor.setVoltageRampRate(VOLT_RAMPUP)

        rr_motor.reverseOutput(True)
        rf_motor.reverseOutput(True)
        lr_motor.reverseOutput(True)
        lf_motor.reverseOutput(True)

        self.stick = wpilib.Joystick(1)

        self.ahrs = AHRS.create_spi()



    def teleopPeriodic(self):

        '''Called on each iteration of the control loop'''

        tm = wpilib.Timer()
        tm.start()

        self.robotDrive.setSafetyEnabled(True)

        if tm.hasPeriodPassed(1.0):
            print("NavX Gyro", self.ahrs.getYaw(), self.ahrs.getAngle())      



                    # The robot does not have a gyro (yeSt) therefore the input is zero
        self.robotDrive.mecanumDrive_Cartesian(self.stick.getX() / 2,
                                               self.stick.getY() / 2,
                                               self.stick.getZ() / 2,self.ahrs.getAngle());

        wpilib.Timer.delay (0.005) #wait for the motor to update


if __name__=='__main__':
    wpilib.run(Bob)

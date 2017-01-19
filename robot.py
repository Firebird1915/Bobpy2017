import wpilib
import ctre
import logging
from networktables import NetworkTable
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



        self.robotDrive.setSafetyEnabled(True)



        self.sd.putBoolean('IsCalibrating', self.ahrs.isCalibrating())
        self.sd.putBoolean('IsConneted',self.ahrs.isConnected())
        self.sd.putNumber('Angle', self.ahrs.getAngle())

        self.sd.putNumber("rr_motor", self.rr_motor.getOutputVoltage())
        self.sd.putNumber("rf_motor", self.rf_motor.getOutputVoltage())
        self.sd.putNumber("lr_motor", self.lr_motor.getOutputVoltage())
        self.sd.putNumber("lf_motor", self.lf_motor.getOutputVoltage())

        wpilib.Timer.delay(0.10)


        print("NavX Gyro", self.ahrs.getYaw(), self.ahrs.getAngle())



                    # The robot does not have a gyro (yeSt) therefore the input is zero
        self.robotDrive.mecanumDrive_Cartesian(self.stick.getX() / 2,
                                               self.stick.getZ() / 2,
                                               -self.stick.getY() / 2,self.ahrs.getAngle());


        wpilib.Timer.delay (0.005) #wait for the motor to update

    def log(self):

        self.logger.info("Entered disabled mode")
        # I really just want to see what we can look at
        self.tm.reset()
        self.tm.start()

        while self.isDisabled():
            if self.timer.hasPeriodPassed(0.5):
                self.sd.putBoolean('IsCalibrating', self.ahrs.isCalibrating())
                self.sd.putBoolean('IsConneted',self.ahrs.isConnected())
                self.sd.putNumber('Angle', self.ahrs.getAngle())

            wpilib.Timer.delay(0.10)


if __name__=='__main__':
    wpilib.run(Bob)

import wpilib
import ctre
import logging
from magicbot import MagicRobot, AutonomousStateMachine
from robotpy_ext.common_drivers import navx
from robotpy_ext.control.button_debouncer import ButtonDebouncer
from wpilib.smartdashboard import SmartDashboard

'''
    Magic bot implimentation
    Things (obviously) are subject to change

    1/27: Using magicbot as main framework this season.
    2/16: drivetrain is a bit more refine.
'''

#Highlevel components before lowlevel components

#lowlevel components
from components.drive import Drive
from components.lift import Lift
from components.dump import Dump

VOLT_RAMPUP = 24/1
MAX_VOLT = 0.5

class Bob(MagicRobot):

    drive = Drive
    lift = Lift
    dump = Dump

    def createObjects(self):

        wpilib.CameraServer.launch('vision.py:main')
        #This lets you spit stuff to the dashboard
        self.sd = wpilib.SmartDashboard

        #Motors and such are set here
        self.rf_motor = ctre.CANTalon(5)
        self.rr_motor = ctre.CANTalon(6)
        self.lf_motor = ctre.CANTalon(2)
        self.lr_motor = ctre.CANTalon(1)

        #Lift
        self.lift_motor = ctre.CANTalon(3)


        self.robotDrive = wpilib.RobotDrive(self.rf_motor,
                                            self.rr_motor,
                                            self.lf_motor,
                                            self.lr_motor)


        self.rf_motor.configMaxOutputVoltage(MAX_VOLT)
        self.rr_motor.configMaxOutputVoltage(MAX_VOLT)
        self.lf_motor.configMaxOutputVoltage(MAX_VOLT)
        self.lr_motor.configMaxOutputVoltage(MAX_VOLT)

        #Prevents the robot from jolting to full power
        self.rf_motor.setVoltageRampRate(VOLT_RAMPUP)
        self.rr_motor.setVoltageRampRate(VOLT_RAMPUP)
        self.lf_motor.setVoltageRampRate(VOLT_RAMPUP)
        self.lr_motor.setVoltageRampRate(VOLT_RAMPUP)

        #makes the motors turn in the correct direction
        self.rr_motor.reverseOutput(True)
        self.rf_motor.reverseOutput(True)
        self.lr_motor.reverseOutput(True)
        self.lf_motor.reverseOutput(True)

        self.doubleS = wpilib.DoubleSolenoid(0,1)
        self.doubleS2 = wpilib.DoubleSolenoid(2,3)

        self.stick = wpilib.Joystick(1) #ps2 controller
        self.stick2 = wpilib.Joystick(2) #logitech joystick

        self.dumperButton = ButtonDebouncer(self.stick, 8)
        self.loaderButton = ButtonDebouncer(self.stick, 6)

        self.compressor = wpilib.Compressor()

        #Navx Gyro (The purple board on the rio)
        self.navX = navx.AHRS.create_spi()
        self.robot = True


    def teleopInit(self):
        #reset the gyro
        self.navX.reset()


    def teleopPeriodic(self):

        '''Called on each iteration of the control loop'''


        if self.robot == True:
            self.compressor.start()

        self.robotDrive.setSafetyEnabled(True)

        wpilib.Timer.delay(0.10)

        try:
            self.drive.move(self.stick.getRawAxis(0),
                            self.stick.getRawAxis(2),
                            -self.stick.getRawAxis(1),
                            self.navX.getAngle(), False)
        except:
            if not self.isFmsAttached():
                raise

        if self.stick.getRawButton(4):
            self.lift.goUp(self.stick.getRawButton(4))
        elif self.stick.getRawButton(1):
            self.lift.goUp(self.stick.getRawButton(1) * .5)
        elif self.stick.getRawButton(2):
            self.lift.goUp(self.stick.getRawButton(2) * -1)
        else:
            self.lift.goUp(self.stick.getRawButton(3) * -.5)

        if self.dumperButton.get():
            self.dump.dumper()
        elif self.loaderButton.get():
            self.dump.loader()

        if self.stick.getRawButton(7):
            self.dump.toggle()

        wpilib.Timer.delay (0.005) #wait for the motor to update


    def log(self):
        self.drive.log(self)

if __name__=='__main__':
    wpilib.run(Bob)

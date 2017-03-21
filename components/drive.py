import wpilib
from robotpy_ext.common_drivers import navx

class Drive:
    """
        handles the process of driving the robot

        This is low level so if you want to touch
        the motors that drive you are in the right
        place.

        Tasks: Arcade drive for autonomous
               Fix logging

    """


    #refrence our drivetrain and gyro via robot.py file
    robotDrive = wpilib.RobotDrive
    navX = navx.AHRS

    def __init__(self):
        pass

    def move(self, x, y, z, angle, squared):
        '''
        Move the robot

        squared: In some cases increase the input before you move
        '''
        if squared:
            if x >= 0.0:
                x *= x
            else:
                x = -(x**2)
            if y >= 0.0:
                y *= y
            else:
                 y = -(y**2)

        self.robotDrive.mecanumDrive_Cartesian(x / 1.2, y / 1.2, z / 1.2, angle)

    def arcade(self, x,y):
        self.robotDrive.arcadeDrive(x,y)


    def log(self):

        #Spit out some data about the gyro
        self.sd.putBoolean('IsCalibrating', self.navX.isCalibrating())
        self.sd.putBoolean('IsConneted',self.navX.isConnected())
        self.sd.putNumber('navx Angle', navX.getAngle())
        self.sd.putNumber("navx Gyro", navX.getYaw())

        #Spit out some data about the drivetrain
        self.sd.putNumber("rr_motor", self.rr_motor.getOutputVoltage())
        self.sd.putNumber("rf_motor", self.rf_motor.getOutputVoltage())
        self.sd.putNumber("lr_motor", self.lr_motor.getOutputVoltage())
        self.sd.putNumber("lf_motor", self.lf_motor.getOutputVoltage())

        

    def execute(self):
        """Actually makes the robot move"""

        #do not move by Default
        self.x = 0
        self.y = 0

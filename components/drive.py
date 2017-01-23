import wpilib
from robotpy_ext.common_drivers import navx
#would import high component here

class Drive:
    """
        handles the process of driving the robot

        This is low level so if you want to touch
        the motors that drive you are in the right
        place.

    """



    robotDrive = wpilib.RobotDrive
    navX = navx.AHRS

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0


    def move(self, x, y, z, angle,):
        '''
        Move the robot
        '''
        self.robotDrive.mecanumDrive_Cartesian(self.x,self.y,self.z, angle)

    def log(self):

        self.logger.info("Robot is enabled: Please dont hurt me or others!")

        self.sd.putBoolean('IsCalibrating', self.navX.isCalibrating())
        self.sd.putBoolean('IsConneted',self.navX.isConnected())
        self.sd.putNumber('navx Angle', navX.getAngle())
        self.sd.putNumber("navx Gyro", navX.getYaw())

        self.sd.putNumber("rr_motor", self.rr_motor.getOutputVoltage())
        self.sd.putNumber("rf_motor", self.rf_motor.getOutputVoltage())
        self.sd.putNumber("lr_motor", self.lr_motor.getOutputVoltage())
        self.sd.putNumber("lf_motor", self.lf_motor.getOutputVoltage())

    def execute(self):

        #You can pass a command through here but it isn't really necessary

        pass

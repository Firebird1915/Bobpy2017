import wpilib
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


class Bob(MagicRobot):

    drive = Drive

    def createObjects(self):
        #Motors and such are set here
        self.rf_motor = rf_motor = wpilib.Talon(1)
        self.rr_motor = rr_motor = wpilib.Talon(2)
        self.lf_motor = lf_motor = wpilib.Talon(3)
        self.lr_motor = lr_motor = wpilib.Talon(4)

        self.robotDrive = wpilib.RobotDrive(rf_motor,
                                            rr_motor,
                                            lf_motor,
                                            lr_motor)
        self.stick = wpilib.Joystick(0)

    def teleopInit(self):
        # optional might be useful later
        pass

    def teleopPeriodic(self):
        '''Called on each iteration of the control loop'''

        self.robotDrive.setSafetyEnabled(True)

            # The robot does not have a gyro (yet) therefore the input is zero
        self.robotDrive.mecanumDrive_Cartesian(self.stick.getX(),
                                               self.stick.getY(),
                                               self.stick.getZ(),0);



if __name__=='__main__':
    wpilib.run(Bob)

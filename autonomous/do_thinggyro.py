from components import drive

from magicbot import AutonomousStateMachine, tunable, timed_state

class doThingGyro(AutonomousStateMachine):

    '''
    Pass the gyro damn it...
    '''

    MODE_NAME = "Do gyro thing"
    Default = False

    drive = drive.Drive

    def initialize(self):
        pass


    @timed_state(duration=3,next_state='turn',first=True)
    def go_foward(self):
        self.drive.arcade(0.5, 0)

    @timed_state(duration=10)
    def turn(self):
        if self.drive.navX.getYaw() > 20:
            self.drive.arcade(0.3,0)
        elif self.drive.navX.getYaw() < 20:
            self.drive.arcade(-0.3,0)

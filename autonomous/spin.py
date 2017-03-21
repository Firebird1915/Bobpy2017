from robotpy_ext.autonomous import StatefulAutonomous, timed_state
from components import drive
from robotpy_ext.common_drivers import navx



from magicbot import AutonomousStateMachine, tunable, timed_state
class MoveForward(AutonomousStateMachine):

    '''
    In StatefulAutonomos the robot will execute a series of events
    in sequential order. This autonomous mode tells SteamBob to move
    for a few seconds and stop.

    Tasks: Probably shouldn't use move for this; will switch to arcade
    '''

    #for dashboard and chooser
    MODE_NAME = 'Spin'
    Default = False

    drive = drive.Drive
    navX = navx.AHRS

    origin_yaw = 1
    first_run = True

    def initialize(self):
        #here we can asign variables for the dashboard
        pass

    @timed_state(duration=5, first=True, next_state="clean_up")
    def turn(self):
        if self.first_run:
            self.origin_yaw = self.drive.navX.getYaw()
            self.first_run = False
        if not (self.drive.navX.getYaw() >= self.origin_yaw + 55):
            self.drive.arcade(0, .5)
    @timed_state(duration=1, first=False)
    def clean_up(self):
        self.first_run = True
        print (self.drive.navX.getYaw(), " ", self.origin_yaw)

from robotpy_ext.autonomous import StatefulAutonomous, timed_state
from components import drive

class MoveForward(StatefulAutonomous):

    '''
    In StatefulAutonomos the robot will execute a series of events
    in sequential order. This autonomous mode tells SteamBob to move
    for a few seconds and stop.

    Tasks: Probably shouldn't use move for this; will switch to arcade
    '''

    #for dashboard and chooser
    MODE_NAME = 'Move Forward'
    Default = False

    drive = drive.Drive

    def initialize(self):
        #here we can asign variables for the dashboard
        pass



    @timed_state(duration=1,next_state='stop', first=True)
    def go_foward(self):
        try:
            self.drive.arcade(0,0.25)
        except:
            if not self.isFmsAttached():
                raise
    @timed_state(duration=5)
    def stop(self):
        self.drive.arcade(0,0)

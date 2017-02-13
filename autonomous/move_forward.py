from robotpy_ext.autonomous import StatefulAutonomos, timed_state

from components.drive import Drive

class MoveForward(StatefulAutonomos):

    '''
    In StatefulAutonomos the robot will execute a series of events
    in sequential order. This autonomous mode tells SteamBob to move
    for a few seconds and stop.
    '''

    #for dashboard and chooser
    MODE_NAME = 'Move Forward'
    Default = False

    drive=Drive

    def initialize(self):
        pass

    @timed_state(duration=1,first=True)
    def go_foward(self):
        drive.move(1,0,0,0)

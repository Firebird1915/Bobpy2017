import wpilib
#would import high component here

class Drive:
    """
        Would handle the process of driving the robot

        For now simply logs that the robot is ready
    """

    def on_enable(self):
        '''Called when the robot enters any mode'''

        self.logger.info("Robot is enabled: Please dont hurt me or others!")

    def execute(self):

        # Would execute something if it had something to execute
        pass

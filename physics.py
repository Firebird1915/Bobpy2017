from pyfrc.physics.drivetrains import two_motor_drivetrain, four_motor_drivetrain

class PhysicsEngine:

    def __init__(self, controller):
        self.controller = controller
        self.controller.add_device_gyro_channel('navxmxp_spi_4_angle')
        self.iErr = 0

    def update_sim(self, hal_data, now, tm_diff):

        l1_motor = hal_data['CAN'][1]['value']/1023
        l2_motor = hal_data['CAN'][2]['value']/1023
        r6_motor = hal_data['CAN'][6]['value']/1023
        r5_motor = hal_data['CAN'][5]['value']/1023

        fwd, rcw = two_motor_drivetrain(l1_motor,r6_motor, speed=5)
        if abs(fwd) > 0.1:
            rcw += -(0.2*tm_diff)
            self.controller.drive(fwd,rcw,tm_diff)

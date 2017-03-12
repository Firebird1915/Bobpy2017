from cscore import CameraServer, VideoSource

"""
Takes in camera via usb source on roborio and
shows us video from two cameras in optimal settings
"""
def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    usb1 = cs.startAutomaticCapture(dev=0)

    usb2 = cs.startAutomaticCapture(dev=1)

    cs.waitForever()

from cscore import cs

"""
nxn
"""
def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    #setup our first camera with settings that won't blow up the RIO

    camera1 = cs.startAutomaticCapture(dev=0) #where the camera is plugged in via usb
    camera1.setVideoMode(cs.VideoMode.PixelFormat.kMJPEG, 320, 240, 20)


    cs.waitForever() #self explanatory

from cscore import CameraServer, UsbCamera

"""
nxn
"""
def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    #setup our first camera with settings that won't blow up the RIO

    usb1 = cs.startAutomaticCapture(dev=0) #where the camera is plugged in via usb
    usb1.setVideoMode(cs.VideoMode.PixelFormat.kMJPEG, 320, 240, 20)

    usb2 = cs.startAutomaticCapture(dev=1)
    usb2.setVideoMode(cs.VideoMode.PixelFormat.kMJPEG, 320, 340, 20)

    cs.waitForever()


if __name__ = '__main__':
    import networktables
    networktables.initialize(server='10.19.15.2')

    main()

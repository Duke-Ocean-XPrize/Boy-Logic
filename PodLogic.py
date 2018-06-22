import time

uniqueID = "drone1"

def inWater():
    return False #Is the buoy in the water?

def getGPS():
    return (0, 0) #Returns the (lat, lon) of the buoy

def broadcast():
    while inWater():
        print getGPS() + "," + uniqueID  #Broadcasts the current position with a period of 0.5 secs
        time.sleep(0.5) #Plan for handling multiple pods broadcasting at once: different pods have slightly different periods (0.51 secs, 0.49 secs, etc),
                        #and the drone listens until it hears three with a certain ID. This way, the drone will definitely hear the nearest broadcasting pod.

def lowerPod():
    pass #lowers the pod, tells it to start pinging

def raisePod():
    pass #above, but in reverse

def pod():
    while not inWater():
        time.sleep(1)
    lowerPod()
    time.sleep(30*60) #sleep for 30 minutes
    raisePod()
    broadcast()

pod()

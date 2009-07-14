import os, sys
import serial
# Add this line if your script is not in your app directory
sys.path.append('/home/josh/adoor/') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'adoor.settings'
from django.conf import settings
from adoor.rfid.models import *

#twitter
from twitter import *
twitter = Twitter("TxRxDoor", "121212")

ser = serial.Serial('/dev/ttyUSB1', 57600)

while 1:
    result = ser.readline()
    trim_result = str(result[:-1])
    trim_result = trim_result[:10]
    print trim_result
    try:
        tag_name = Tag.objects.get(rfid_tag__startswith=trim_result)
        if tag_name.enabled:
            ser.write("1")
            print "Tag enabled, door will open"
            twitter.statuses.update(status=tag_name.name + " has entered the space")
            #should update the last seen field on the tag object
            #also add audit logs
            #send tweets
        else:
            ser.write("0")
            print "Tag disabled, door will not open"
    except: #this needs to only fail for items not found not a general except
        ser.write("0")
        print "The tag was not found"
    
import serial
import time

data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
path = '/dev/cu.usbserial-FTCBGW24'
try:
    port = serial.Serial(path, 300)
    bytesWritten = port.write(data)
    if bytesWritten == len(data):
        print('Wrote to port: %s' % port.name)
    else:
        print('Error when writing to port: %s' % port.name)

    time.sleep(1)
    port.close()
except IOError:
    print('Unable to open the port with path: %s' % path)
except:
    print('Unknown error')

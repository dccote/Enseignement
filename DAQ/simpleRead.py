import serial

text = 'hello'
path = '/dev/cu.usbserial-FTCBGW24'
try:
    port = serial.Serial(path)
    bytesRead = port.read(text)

    if bytesRead == len(text):
        print('Wrote to port: %s' % port.name)
    else:
        print('Error when writing to port: %s' % port.name)

    port.close()
except IOError:
    print('Unable to open the port with path: %s' % path)
except:
    print('Unknown error')

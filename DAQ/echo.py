import serial

text = 'hello'
path = '/dev/cu.usbserial-FTCBGW24'
try:
    port = serial.Serial(path)
    bytesWritten = port.write(text)

    if bytesWritten == len(text):
        print('Wrote to port: %s' % port.name)
    else:
        print('Error when writing to port: %s' % port.name)

    echo = port.read(bytesWritten)

    if bytesWritten == len(echo):
        print('Read from port: %s ' % echo)
    else:
        print('Error when reading to port: %s' % port.name)

    port.close()
except IOError:
    print('Unable to open the port with path: %s' % path)
except:
    print('Unknown error')

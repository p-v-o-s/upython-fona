import board
from busio import UART
import utime

FONA_BAUD=4800

uart=UART(board.D0,board.D2,baudrate=FONA_BAUD) # for UART2 on esp32 dev board, RX:16, TX:17
uart.init(FONA_BAUD)

# clear the buffer
for i in range(3):
    uart.readline()

# check replies
for i in range(10):
    message="AT" 
    uart.write(message+'\r\n') # \r and \n seem necessary
    print(">>\n"+message)
    utime.sleep(.1)
    response=uart.read().decode('ascii')
    print("<<")
    print(response.split())
    utime.sleep(.1)


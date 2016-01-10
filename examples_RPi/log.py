#!/usr/bin/env python

# Log Mode
#
# Example using Dynamic Payloads
# 
#  This is an example of how to use payloads of a varying (dynamic) size.
# 

import time
import logging
from RF24 import *

# Setup for GPIO 22 CE and CE1 CSN with SPI Speed @ 8Mhz
radio = RF24(RPI_V2_GPIO_P1_15, BCM2835_SPI_CS0, BCM2835_SPI_SPEED_8MHZ)

print 'pyRF24/examples/pingpair_dyn/'
radio.begin()
radio.enableDynamicPayloads()
radio.setDataRate(RF24_1MBPS) #best performance / distance option
radio.setChannel(76)
radio.setCRCLength(RF24_CRC_16)
radio.setRetries(15,15)
radio.printDetails()
radio.setAutoAck(1)
radio.openWritingPipe(pipes[1])
radio.openReadingPipe(1,pipes[0])
radio.startListening()

while 1:
        if radio.available():
            while radio.available():
                # Fetch the payload, and see if this was the last one.
	            len = radio.getDynamicPayloadSize()
	            receive_payload = radio.read(len)

	            # Spew it
	            print 'Got payload size=', len, ' value="', receive_payload, '"'
            		    logging.basicConfig(filename='/home/pi/Desktop/Log.txt',level=logging.INFO,format'%(asctime)s	%(message)s',datefmt='%d.%m.%Y	%H:%M:%S') #txt format for access autoimport compatibility
                    logging.info(receive_payload)
                    time.sleep(0.5) #make it 1.5 if you have a node network greater than 150 nodes

            # First, stop listening so we can talk
            radio.stopListening()

            # Send the final one back.
            #radio.write(receive_payload) #enable if necessary
            #print 'Sent response.' #enable if necessary

            # Now, resume listening so we catch the next packets.
            radio.startListening()

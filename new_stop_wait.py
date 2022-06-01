# Bonus Assignment 1 for Data Communications Networking
# simulation of the Stop & Wait protocol
# by J-Waal

import asyncio
from queue import Queue
import random
import time

# class for data-frame
class Frame:
    def __init__(self, framenumber, data) -> None:
        self.framenumber = framenumber
        self.data = data
    def string(self):
        return f'{self.framenumber}.{self.data}'

def bernuolli(p): # Bernoulli function the simulate coruption
    x = random.choices([0,1], weights=[p,1-p])
    return(x[0])

# channel delay function, also simulate packet loss
async def sendAfter(delay: float, queue: Queue, frame: Frame, P: float):
    await asyncio.sleep(delay)
    if bernuolli(P)==1: # only send the frame if no corruption did apear
        await queue.put(frame)

# sender function
async def sender(p1, delay, timeout, sender_receiver: Queue, receiver_sender: Queue):
    dataToSend = [1,4,1,5,9,2,6,5,3,5] # we want to send this 10 values as packets
    n_s = 0 # use bitwise operation limited to a finite field
    times_send: int = 0
    times_timeout: int = 0
    for item in dataToSend:
        # create dataframe
        outgoingFrame = Frame(n_s,item)
        print(f"sender:\t\tsend frame, {outgoingFrame.string()}")
        while True:
            asyncio.ensure_future(sendAfter(delay,sender_receiver,outgoingFrame,p1))
            times_send += 1 # keep track of how many data frames are send (only used for analysis purpose)
            # wait for the response
            try:
                responseFrame: Frame = await asyncio.wait_for(receiver_sender.get(), timeout=timeout) # timeout
                print(f"sender:\t\treceived response, {responseFrame.string()}")
                n_s = n_s ^ 1 # update N_s, bitwise xor
                print("sender:\t\treceived ACK, sending next frame")
                break
            except asyncio.TimeoutError:
                print('sender:\t\ttimeout, resend frame')
                times_timeout += 1 # (only used for analysis purpose)
    print("sender:\t\tall data successfully transmitted")
    print(f"sender:\t\tneeded to send {times_send} frames") # for analysis
    print(f"sender:\t\tan timeout did occur {times_timeout} times") # for analysis
    return times_send

# receiver function
async def receiver(p2, delay, sender_receiver: Queue, receiver_sender: Queue):
    n_r = 0 # use bitwise operation limited to a finite field
    receivedData = [] # emty list to store the incoming 
    while True: # The receiver will always listen for incoming frames
        incomingFrame: Frame = await sender_receiver.get()
        if incomingFrame.data == 'stop': # check for the stop command
            break # stop the receiver when an stop command is detected 
        print(f"receiver:\treceived frame, {incomingFrame.string()}")
        # check if the frame number is matching the expected frame
        if incomingFrame.framenumber == n_r:
            receivedData.append(incomingFrame.data)
            n_r = n_r ^ 1 # update N_r, bitwise xor
            print("receiver:\tvalid frame received")
        else:
            print("receiver:\t duplicate frame received, discard")
        # always send ACK
        ackFrame = Frame(n_r,incomingFrame.data)
        print(f"receiver:\tsending ACK, {ackFrame.string()}")
        asyncio.ensure_future(sendAfter(delay,receiver_sender,ackFrame,p2))
    print(f"receiver:\tall data received, {receivedData}")
    return receivedData


async def main(p1, p2, delay, timeout):
    sender_receiver = asyncio.Queue()
    receiver_sender = asyncio.Queue()
    # run both the sender and the receiver concurrent
    senderTask = asyncio.create_task(sender(p1, delay, timeout, sender_receiver, receiver_sender))
    receiverTask = asyncio.create_task(receiver(p2, delay, sender_receiver, receiver_sender))
    await senderTask # wait for the sender to recive an ACK for all items
    # when the sender is done, the receiver can also stop. to do this in the simulation we send an stop command.
    await sender_receiver.put(Frame('x','stop'))
    await receiverTask # wait for the receiver to shutdown and return the result

if __name__ == '__main__':
    p1 = 0.1
    p2 = 0.1
    delay = 0.1
    timeout = 0.5
    start_time = time.time()
    asyncio.run(main(p1, p2, delay, timeout))
    print("--- %s seconds ---" % (time.time() - start_time))

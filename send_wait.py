print('hello world')
print('program start')

import asyncio
from queue import Queue
import random

# data frame class
class Frame:
    def __init__(self, corrupted: int, framenumber: int, data: int) -> None:
        self.corrupted = corrupted
        self.framenumber = framenumber
        self.data = data
    def string(self):
        return f'{self.corrupted}.{self.framenumber}.{self.data}'

def bernuolli(p): # Bernoulli function the simulate coruption
    x = random.choices([0,1], weights=[p,1-p])
    return(x[0])

# sender function
async def sender(p1, sender_receiver: Queue, receiver_sender: Queue):
    dataToSend = [1,4,1,5,9,2,6,5,3,5] # we want to send this 10 packets
    n_s = 0
    times_send = 0
    for item in dataToSend:
        # create dataframe
        outgoingFrame = Frame(1,n_s,item)
        print(f"sender:\t\tsend frame, {outgoingFrame.string()}")
        while True:
            # see if the frame gets corrupted
            outgoingFrame.corrupted = bernuolli(p1)
            await sender_receiver.put(outgoingFrame)
            times_send += 1
            # wait for the response
            responseFrame: Frame = await receiver_sender.get() # timeout?
            print(f"sender:\t\treceived response, {responseFrame.string()}")
            # see if any corruption did occur
            if responseFrame.corrupted == 1:
                print("sender:\t\treceived ACK, sending next frame")
                n_s = n_s ^ 1
                break
            else:
                print("sender:\t\terror, resend frame")
    print("sender:\t\tall data successfully transmitted")
    print(f"sender:\t\tneeded to send {times_send} frames")
    return times_send



# receiver function
async def receiver(p2, sender_receiver: Queue, receiver_sender: Queue):
    n_r = 0
    receivedData = []
    while len(receivedData) < 10: # stop after we have 10 packets
        incomingFrame: Frame = await sender_receiver.get()
        print(f"receiver:\treceived frame, {incomingFrame.string()}")
        # see if frame is valid
        if incomingFrame.corrupted == 1:
            # do check on framenumbner
            if incomingFrame.framenumber == n_r:
                receivedData.append(incomingFrame.data)
                n_r = n_r ^ 1
                print("receiver:\tvalid frame received")
            else:
                print("receiver:\t duplicate frame received, discard")
            # send ACK
            ackFrame = Frame(1,n_r,incomingFrame.data)
            print(f"receiver:\tsending ACK, {ackFrame.string()}")
            # see if the ACK frame gets corrupted
            ackFrame.corrupted = bernuolli(p2)
        else:
            print("receiver:\tcorrupted frame received, discard")
            # send corupted frame
            ackFrame = Frame(0,n_r,incomingFrame.data)
        await receiver_sender.put(ackFrame)
    print(f"receiver:\tall data received, {receivedData}")
    # close comunication
    await receiver_sender.put(Frame(1,'x','x'))
   

async def main(p1, p2):
    sender_receiver = asyncio.Queue()
    receiver_sender = asyncio.Queue()
    await asyncio.gather(
        sender(p1, sender_receiver, receiver_sender),
        receiver(p2, sender_receiver, receiver_sender)
    )

if __name__ == '__main__':
    p1 = 0.5
    p2 = 0.5
    asyncio.run(main(p1, p2))

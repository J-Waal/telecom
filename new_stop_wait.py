print('hello world')
print('program start')

import asyncio
from queue import Queue
import random
import time

# data frame class
class Frame:
    def __init__(self, framenumber: int, data: int) -> None:
        self.framenumber = framenumber
        self.data = data
    def string(self):
        return f'{self.framenumber}.{self.data}'

def bernuolli(p): # Bernoulli function the simulate coruption
    x = random.choices([0,1], weights=[p,1-p])
    return(x[0])

# channel delay function
async def sendAfter(delay: float, queue: Queue, frame: Frame):
    await asyncio.sleep(delay)
    await queue.put(frame)

# sender function
async def sender(p1, delay, timeout, sender_receiver: Queue, receiver_sender: Queue):
    dataToSend = [1,4,1,5,9,2,6,5,3,5] # we want to send this 10 values as packets
    n_s = 0
    times_send = 0
    times_timeout = 0
    for item in dataToSend:
        # create dataframe
        outgoingFrame = Frame(n_s,item)
        print(f"sender:\t\tsend frame, {outgoingFrame.string()}")
        while True:
            # see if the frame gets corrupted
            if bernuolli(p1) == 1:
                # only send the frame if no corruption did apear
                asyncio.ensure_future(sendAfter(delay,sender_receiver,outgoingFrame))
            times_send += 1 # keep track of how many data frames are send
            # wait for the response
            try:
                responseFrame: Frame = await asyncio.wait_for(receiver_sender.get(), timeout=timeout) # timeout
                print(f"sender:\t\treceived response, {responseFrame.string()}")
                n_s = n_s ^ 1 # increment N_s
                print("sender:\t\treceived ACK, sending next frame")
                break
            except asyncio.TimeoutError:
                print('sender:\t\ttimeout, resend frame')
                times_timeout += 1
    print("sender:\t\tall data successfully transmitted")
    print(f"sender:\t\tneeded to send {times_send} frames")
    print(f"sender:\t\tan timeout did occur {times_timeout} times")
    return times_send

# receiver function
async def receiver(p2, delay, sender_receiver: Queue, receiver_sender: Queue):
    n_r = 0
    receivedData = []
    while len(receivedData) < 10: # stop after we have 10 packets
        incomingFrame: Frame = await sender_receiver.get()
        print(f"receiver:\treceived frame, {incomingFrame.string()}")
        # do check on framenumbner
        if incomingFrame.framenumber == n_r:
            receivedData.append(incomingFrame.data)
            n_r = n_r ^ 1
            print("receiver:\tvalid frame received")
        else:
            print("receiver:\t duplicate frame received, discard")
        # send ACK
        ackFrame = Frame(n_r,incomingFrame.data)
        print(f"receiver:\tsending ACK, {ackFrame.string()}")
        # see if the ACK frame gets corrupted
        if bernuolli(p2) == 1:
            # only send the ACK if no corruption did apear
            asyncio.ensure_future(sendAfter(delay,receiver_sender,ackFrame))
    print(f"receiver:\tall data received, {receivedData}")
    # close comunication
    await receiver_sender.put(Frame('x','x'))


async def main(p1, p2, delay, timeout):
    sender_receiver = asyncio.Queue()
    receiver_sender = asyncio.Queue()
    sender
    await asyncio.gather(
        sender(p1, delay, timeout, sender_receiver, receiver_sender),
        receiver(p2, delay, sender_receiver, receiver_sender)
    )

if __name__ == '__main__':
    p1 = 0.1
    p2 = 0.1
    delay = 0.1
    timeout = 0.5
    start_time = time.time()
    asyncio.run(main(p1, p2, delay, timeout))
    print("--- %s seconds ---" % (time.time() - start_time))

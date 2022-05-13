from statistics import NormalDist
import math as np

#question 1
print("question 1")

transmission_rate_kbit = 750 # kbit/sec
alpha = 4.5
beta = 3.2
noise_psd_dbm = -91 # dBm/Hz
snr_in_db = 9.5 # dB

# see homework 4
# part a
noise_power_mw = ((transmission_rate_kbit*1e3)/2)*10**(noise_psd_dbm/10)
noise_power_dbm = 10*np.log10(noise_power_mw)
#print(noise_power_dbm)
signal_power_in_dbm = noise_power_dbm + snr_in_db
print(f"signal_in: {signal_power_in_dbm:.2f} dBm")

# part b
effectiveness = (beta**2)/(alpha**2+beta**2)
# part c


print("")

#question 2
print("question 2")
##Ik doe vraag 2 wel wanneer ik thuiskom -Guus

# part a


# part b

print("")

#question 3
print("question 3")


# part a


# part b

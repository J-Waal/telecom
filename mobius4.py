# mobius 4
import numpy as np

# question 1
print("question 1")
baseband_BW = 13000 # hz
delta_F = 35000 # hz
m2t_V2p = 0.7
PSDnoise_double = -93.5 # dBm
receiver_in_pow = -21 # dBm

# part a

# lecture 3 slide 24
# rewrite to eliminate beta
Carson_BW = 2*(baseband_BW+delta_F)


PSDnoise_single = PSDnoise_double + 10*np.log10(2)

DB_herz = 10*np.log10(Carson_BW)
total_noise = PSDnoise_single + DB_herz

IF_snr = receiver_in_pow - total_noise

print(f"IF_snr = {IF_snr} dB")

# lecture 3 slide 14
beta = delta_F / baseband_BW

#calculating AC
ac_squared  = 2*10**(receiver_in_pow)

# lecture 4 slide 19
demodulated_snr = (3*ac_squared*beta**2*m2t_V2p)/(2*10**(PSDnoise_single)*1000*baseband_BW)

print(f"demodulated_snr = {demodulated_snr} dB")

# part b

# question 2
print("question 2")
bitrate = 220 # kbit/s
amplitude = 55 # V  # peak amplitude
resistance = 140 # ohm
modulation = 0.3 # rad/v
# part a

first_null_null_BW = 2 * bitrate
print(f"first_null_null_BW = {first_null_null_BW} kHz")

# part b

power = amplitude**2/2/resistance
print(f"power = {power} W")

# part c
# lecture 4 slide 35
carrier_comp = np.cos(modulation*np.pi)*100
print(f"carrier_comp = {carrier_comp} %")


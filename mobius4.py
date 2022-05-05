# mobius 4
import math as np

# question 1
print("question 1")
baseband_BW = 13 # khz
delta_F = 35 # khz
m2t_V2p = 0.7
PSDnoise_double = -93.5 # dBm
receiver_in_pow = -21 # dBm
IF_filter = 1.5

# part a

# lecture 3 slide 24
# rewrite to eliminate beta
Carson_BW = 2*(baseband_BW+delta_F)*1000 # in hz


PSDnoise_single = PSDnoise_double + 10*np.log10(2) # +3 dB

DB_herz = 10*np.log10(IF_filter*Carson_BW)

total_noise = PSDnoise_single + DB_herz 

IF_snr = receiver_in_pow - total_noise

print(f"IF_snr = {IF_snr:.3f} dB")

# lecture 3 slide 14
beta = delta_F / baseband_BW

#calculating AC
ac_squared  = 2*10**((receiver_in_pow-30)/10)
#print(f"AC_squared = {ac_squared}")

# lecture 4 slide 16
demodulated_snr = 10*np.log10((3*ac_squared*beta*beta*m2t_V2p)/(2*10**((PSDnoise_single-30)/10)*baseband_BW))


print(f"demodulated_snr = {demodulated_snr:.3f} dB")

# part b
Ps=delta_F**2 * m2t_V2p

Bbb=2*baseband_BW
Pn=2/3/ac_squared * 10**((PSDnoise_single-30)/10) * Bbb**3

SNRout=Ps/Pn
print(f"snr_out = {10*np.log10(SNRout):.3f} dB")

# question 2
print("question 2")
bitrate = 220 # kbit/s
amplitude = 55 # V  # peak amplitude
resistance = 140 # ohm
modulation = 0.3 # rad/v
nth_null = 1
# part a

nth_null_null_BW = 2 * bitrate * nth_null
print(f"nth_null_null_BW = {nth_null_null_BW} kHz")

# part b

power = amplitude**2/2/resistance
#print(f"power = {power:.3f} W")
print(f"power = {10*np.log10(power*1e3):.3f} dBm")

# part c
# lecture 4 slide 35
carrier_comp = np.cos(modulation*np.pi)*100
print(f"carrier_comp = {carrier_comp:.2f} %")
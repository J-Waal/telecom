#mobius 5
import math as np
import rlcompleter

#question 1
bit_rate = 190000 #bits/s
modulation_type = 1 #1 for QAM, 2 for QPSK
#WARNING: EXTRA USER INPUT NEEDED FOR QUESTION C
QAM_order = 128 #
#a
if (modulation_type == 1):
    bits_per_symbol = (np.log2(QAM_order))
elif (modulation_type == 2):
    bits_per_symbol = 2

print(f"bits per symbol: {bits_per_symbol} bits")

#b
null_to_null_bandwidth = 2*bit_rate/bits_per_symbol #in hertz, slide 12
print(f"null-to-null bandwidth: {null_to_null_bandwidth/1000} kHz")

#c
QAM_order_2 = 64
rolloff_factor = 0.85

transmission_bandwidth = bit_rate/(np.log2(QAM_order_2))*(1+rolloff_factor)
print(f"transmission bandwidth: {transmission_bandwidth/1000} kHz")
spectral_efficiency
#question 2
#a

#b

#c

#question 3
#a

#b

#c

#d

#question 4
#a

#b

#c
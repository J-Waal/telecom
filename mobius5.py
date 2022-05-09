#mobius 5
import math as np
import rlcompleter

#question 1
print("question 1")
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
print(f"null-to-null bandwidth: {null_to_null_bandwidth/1000:.3f} kHz")

#c
QAM_order_2 = 64
rolloff_factor = 0.85

transmission_bandwidth = bit_rate/(np.log2(QAM_order_2))*(1+rolloff_factor)
print(f"transmission bandwidth: {transmission_bandwidth/1000:.3f} kHz")
#spectral_efficiency

#question 2
print("question 2")
bit_rate_2 = 280 # kbit/sec
delta_f = 160 # khz
droped_db = -16.5 # dB

#a
# lecture 4 slide 49
null_to_null_bandwidth_2 = 2*delta_f+2*bit_rate_2 # this calculation is in khz
print(f"null-to-null bandwidth: {null_to_null_bandwidth_2} kHz")

#b
# lecture 5 slide 18
new_bitrate = 4* delta_f # implicit kilo term
print(f"new bitrate: {new_bitrate} kbit/sec")
#print(f"new null-null bandwidth: {2*delta_f+new_bitrate} kHz")
#print(1.5*new_bitrate) # ?

#c
# lecture 5 slide 23
# hard one, use wolfram alpha

#question 3
print("question 3")
subcarriers = 51
bandwith = 43 # Mhz
n_psk = 8
n_psk_2 = 8 # given in part d

#a
# lecture 5 slide 35
r_ss = (bandwith*1e6)/(subcarriers+1)
print(f"r_ss: {r_ss/1e3:.4f} kBaud")

#b
total_bitrate = r_ss*subcarriers*np.log2(n_psk)
print(f"r_ss: {r_ss/1e6:.4f} Mbit/sec")

#c
spectral_efficiency = total_bitrate/(bandwith*1e6)
print(f"spectral efficiency: {spectral_efficiency} bits/s/Hz")

#d
new_bautrate = total_bitrate/np.log2(n_psk_2)
new_bandwith = 2 * new_bautrate
#print(f"new bandwidth: {new_bandwith} Hz")
new_spectral_efficiency = total_bitrate/new_bandwith
print(f"new spectral efficiency: {new_spectral_efficiency} bits/s/Hz")

#question 4
print("question 4")
bit_rate_3_kbit = 260 # kbit/s
signal_power_dbm = -9 # dBm
modulation_technique = "OOK" # given in part a
offset_frequency_khz = +52 # kHz, given in part b
#a
if (modulation_technique in {"OOK", "BPSK"}):
    #lecture 5 slide 25
    print(f"null-to-null bandwidth: {2*bit_rate_3_kbit} kHz")
    print("spectral efficiency: 0.5 bits/sec/Hz")
else:
    print("onbekende techniek (feel free to submit a pull request)")
#b
bit_rate_3 = bit_rate_3_kbit*1000
offset_frequency = offset_frequency_khz*1000
signal_power_mw = 10**(signal_power_dbm/10) # in mW
#print(f"recived power: {signal_power_mw}")
if modulation_technique == "OOK":
    # lecture 4 slide 30
    psd_mw = (signal_power_mw/2)*(np.sin(offset_frequency/bit_rate_3*np.pi)/(offset_frequency/bit_rate_3*np.pi))**2/bit_rate_3
    #print(f"power spectral density: {psd_mw} mW/Hz")
    psd_dbm = 10*np.log10(psd_mw)
    print(f"power spectral density: {psd_dbm} dBm/Hz")
    pass
else:
    pass
#c


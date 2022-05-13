from statistics import NormalDist
import math as np

#question 1
print("question 1")

transmission_rate_kbit = 750 # kbit/sec
alpha = 4.5
beta = 3.2
noise_psd_dbm = -91 # dBm/Hz
snr_in_db = 9.5 # dB
equivalent_noise_bandwidth_mult = 0.8 # *Rs, found in part c

# see homework 4
# part a
noise_power_mw = ((transmission_rate_kbit*1e3)/2)*10**(noise_psd_dbm/10)
noise_power_dbm = 10*np.log10(noise_power_mw)
#print(noise_power_dbm)
signal_power_in_dbm = noise_power_dbm + snr_in_db
print(f"signal_in: {signal_power_in_dbm:.2f} dBm")

# part b
signal_power_in_mw = 10**(signal_power_in_dbm/10)
# signal can be seen as an data copmonent carier
effectiveness = (beta**2)/(alpha**2+beta**2)
#print(effectiveness)
# convert to a BPSK signal
signal_power_effective = signal_power_in_mw*effectiveness # in mw
noise_psd = 10**(noise_psd_dbm/10) # mw/Hz
#lecture 7 slide 15 and homework 4
two_Eb_over_N0 = 2*signal_power_effective/noise_psd/(transmission_rate_kbit*1e3)
#print(two_Eb_over_N0)
error_probability_MF = 1-NormalDist(0,1).cdf(np.sqrt(two_Eb_over_N0))
print(f"error probability: {error_probability_MF}")

# part c
#lecture 7 slide 14
equivalent_noise_bandwidth = transmission_rate_kbit*1e3*equivalent_noise_bandwidth_mult
a2_over_2nb_eq = signal_power_effective/(noise_psd*equivalent_noise_bandwidth)
#print(a2_over_2nb_eq)
error_probability_nb = 1-NormalDist(0,1).cdf(np.sqrt(a2_over_2nb_eq))
print(f"error probability: {error_probability_nb}")
print("")

#question 2
print("question 2")


# part a


# part b

print("")

#question 3
print("question 3")


# part a


# part b

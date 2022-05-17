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
data_rate = 660 #kbit/s
N0 = 20 #WARNING: pW/Hz
Pe1 = 4*10**(-4) #bit error probability q1
BEF1 = 4 #detection filter factor

# part a


# part b

print("")

#question 3
print("question 3")
# some extra variables are printed for testing
data_rate_kbit_3 = 180 # kbit/sec
alpha_3  = 3.5
beta_3 = 1.75
noise_psd_2side_dbm = -83 # dBm/Hz
ac2_over2_dbm = -28 # dBm, found in part a
given_snr_db = 7 # dB, found in part b

# part a
total_power = 10**(ac2_over2_dbm/10)
print(f"total signal power: {total_power:.2e} mw")

# in-phase power
power_in_phase_mw = (alpha_3**2/(alpha_3**2+beta_3**2)) * total_power
print(f"In-phase power:   {power_in_phase_mw:.6f} mw, {10*np.log10(power_in_phase_mw):.2f} dBm")
# quadrature power
power_quadrature_mw = (beta_3**2/(alpha_3**2+beta_3**2)) * total_power
print(f"Quadrature power: {power_quadrature_mw:.6f} mw, {10*np.log10(power_quadrature_mw):.2f} dBm")

# check to see if the total power match
print(f"I+Q signal power:   {(power_in_phase_mw+power_quadrature_mw):.2e} mw")

# single sided power spectral density
noise_psd_mw_3 = 2 * 10**(noise_psd_2side_dbm/10) # single side PSD in mw
print(f"single sided power spectral density: {noise_psd_mw_3:.2e} mw/Hz")

# filter bandwith
filter_bw = (data_rate_kbit_3*1e3)/4

# noise power
noise_power_mw_3 = (noise_psd_mw_3*filter_bw)
print(f"noise power: {noise_power_mw_3:.6f} mw")

# signal-to-noise ratio
calculated_snr = power_in_phase_mw/noise_power_mw_3
calculated_snr_db = 10*np.log10(calculated_snr)
print(f"calculated in-phase snr: {calculated_snr_db:.2f} dB")

print("")
# part b
symbolrate = data_rate_kbit_3*1e3/2

snr_i = 10**(given_snr_db/10)
snr_q = snr_i/alpha_3**2*beta_3**2
print(f"SNR I: {snr_i:8.3f}, Q: {snr_q:8.3f}")
print(f"SNR I: {10*np.log10(snr_i):5.2f} dB, Q: {10*np.log10(snr_q):5.2f} dB")

# lectue 7 slide 15
# we use that SNR = (A^2)/(2*N_0*BW)
# so 2*T*SNR*BW = (T*A^2)/(N_0), where T is the symbol time
# = (2*SNR*BW)/R, where R is the symbol rate = bitrate/2

ndist = NormalDist(0,1) # store the object to make the cdf notation short

in_phase_error =   ndist.cdf(-np.sqrt(2*snr_i*filter_bw/symbolrate))
quadrature_error = ndist.cdf(-np.sqrt(2*snr_q*filter_bw/symbolrate))
print(f"error I: {in_phase_error}, Q: {quadrature_error}")
# average bit error probability
total_ber = 0.5*in_phase_error+0.5*quadrature_error
print(f"average bit error probability {total_ber*100:.4f} %")
# https://www.unilim.fr/pages_perso/vahid/notes/ber_awgn.pdf

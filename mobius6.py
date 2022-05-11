from statistics import NormalDist
import math as np

#question 1
print("question 1")

noise_mean = 0
noise_rms = 1.6 # found in part a
# WARNING! MADE A MISTAKE USING VARIANCE INSTEAD OF SD
# also rms is not equal to the variance when the mean is not 0
false_alarm_probability_percent = 2 # %, found in part a
airplane_reflected = 3.4 # volt, found in part b
detection_probability_percent = 99 # %, found in part c

# part a
threshold_voltage = NormalDist(noise_mean,noise_rms).inv_cdf(1-false_alarm_probability_percent/100)
print(f"threshold_voltage: {threshold_voltage*1e3} mV")

# part b
probability_missed = NormalDist(airplane_reflected,noise_rms).cdf(threshold_voltage)
print(f"probability missed: {probability_missed*100} %")

# part c
reflected_signal=NormalDist(threshold_voltage,noise_rms).inv_cdf(detection_probability_percent/100)
print(f"reflected signal: {reflected_signal*1e3} mV")

print("")

#question 2
print("question 2")

a_amplitude = 6.5 # V
v_negative_t = -5.05 # V
v_positive_t = 4.95 # V
noise_sd = 1.4 # V

# part a
signal_power = a_amplitude**2
noise_power = noise_sd**2
snr_db = 10*np.log10(signal_power/noise_power)
print(f"SNR: {snr_db} dB")
# part b
p_error1 = 1-NormalDist(-a_amplitude,noise_sd).cdf(v_negative_t)
p_error2 = NormalDist(a_amplitude,noise_sd).cdf(v_positive_t)
p_errort = p_error1*0.5+p_error2*0.5 #lecture 6 slide 18 and also probstat
print(f"Pe1: {p_error1}")
print(f"Pe2: {p_error2}")
print(f"Pet: {p_errort}")
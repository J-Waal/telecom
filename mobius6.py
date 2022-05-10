from statistics import NormalDist
import math as np

#question 1
print("question 1")

noise_mean = 0
noise_rms = 1.4 # found in part a
# WARNING! MADE A MISTAKE USING VARIANCE INSTEAD OF SD
# also rms is not equal to the variance when the mean is not 0
false_alarm_probability_percent = 6 # %, found in part a
airplane_reflected = 3.7 # volt, found in part b
detection_probability_percent = 99 # %, found in part v

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

a_amplitude = 11.5 # V
v_negative_t = -3.85 # V
v_positive_t = 4.25 # V
noise_sd = 1 # V

# part a
signal_power = a_amplitude**2
noise_power = noise_sd**2
snr_db = 10*np.log10(signal_power/noise_power)
print(f"SNR: {snr_db} dB")
# part b
p_error1 = 1-NormalDist(-a_amplitude,noise_sd).cdf(v_negative_t)
p_error2 = NormalDist(a_amplitude,noise_sd).cdf(v_positive_t)

print(p_error1,p_error2)
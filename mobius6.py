from statistics import NormalDist

#question 1
print("question 1")

noise_mean = 0
noise_rms = 1.4 # found in part a
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
# part a
# part b

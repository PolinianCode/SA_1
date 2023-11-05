from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import random

class Measure:
    def __init__(self, cycles, signal_samples, measure_samples, noise_spread = 0.2):
        self.t_signal = np.linspace(0, cycles*2*np.pi, signal_samples) # create time axis for original signal
        self.y_signal = signal.sawtooth(self.t_signal, 0.5) # y - triangle original function 

        self.t_measure = np.linspace(0, cycles*2*np.pi, measure_samples) # create time axis for measurement
        self.y_measure = []

        #iterate over original signal and add some noise
        for i in range(0, len(self.y_signal), signal_samples//measure_samples):
            noise = ( random.random() - 0.5 ) * noise_spread 
            self.y_measure.append(self.y_signal[i] + noise) 

    def filter_signal(self, H = 4):
        filtered_signal = []
        for i in range(0, len(self.y_measure)-H):
            counted_average = np.sum(self.y_measure[i:i+H]) / H # sum of H elements divided by H (average)
            filtered_signal.append(counted_average) #! needed to be the same size as t_measure (+ H of nones)

        return filtered_signal    
    
            


pomiar = Measure(3, 250, 125)


plt.plot(pomiar.t_signal, pomiar.y_signal)
#plt.plot(pomiar.t_measure, pomiar.y_measure, '.')
plt.plot(pomiar.t_signal, pomiar.filter_signal())
plt.show()
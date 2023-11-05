from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import random

class Measure:
    def __init__(self, cycles, signal_samples, measure_samples, noise_spread=0.3):
        self.t_signal = np.linspace(0, cycles * 2 * np.pi, signal_samples)
        self.y_signal = signal.sawtooth(self.t_signal, 0.5)

        self.t_measure = np.linspace(0, cycles * 2 * np.pi, measure_samples)
        self.y_measure = []

        for i in range(0, len(self.y_signal), signal_samples // measure_samples):
            noise = (random.random() - 0.5) * noise_spread
            self.y_measure.append(self.y_signal[i] + noise)

h = 5  
pomiar = Measure(3, 250, 125)

def sredniaRuchoma(probki, h):
    return np.convolve(probki, np.ones(h) / h, mode='same')[:len(probki)]

filtered_signal = sredniaRuchoma(pomiar.y_measure, h)

plt.plot(pomiar.t_signal, pomiar.y_signal, label='Original Signal')
#plt.plot(pomiar.t_measure, pomiar.y_measure, '.', label='Noisy Measured Signal')
plt.plot(pomiar.t_measure, filtered_signal, 'g--', label='Filtered Signal')
plt.legend()
plt.show()

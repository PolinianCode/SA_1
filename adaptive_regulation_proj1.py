from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import random

def MSE(original, data):
    N = len(original)
    sum = 0
    for i in range(0, N):
        if data[i] is not None:
            sum += (original[i]-data[i])**2
    
    result = sum/N
    
    return result
    

class Measure:
    def __init__(self, cycles, signal_samples, measure_samples, noise_spread = 0.2):
        self.t_signal = np.linspace(0, cycles*2*np.pi, signal_samples) # create time axis for original signal
        self.y_signal = signal.sawtooth(self.t_signal, 0.5) # y - triangle original function 

        self.t_measure = np.linspace(0, cycles*2*np.pi, measure_samples) # create time axis for measurement
        self.y_measure = signal.sawtooth(self.t_measure, 0.5)

        #iterate over original signal and add some noise
        for i in range(0, len(self.y_measure)):
            noise = ( random.random() - 0.5 ) * noise_spread 
            self.y_measure[i] += noise 

    def filter_signal(self, H):
        self.H = H

        self.y_filtered = [None] * len(self.y_measure)
        self.filtered_data = []

        for i in range(0, len(self.y_measure)-H):
            step_mean = (np.sum(self.y_measure[i:i+H]))/H
            self.filtered_data.append(step_mean)
        
        filtered_start_point = (H//2)
        filtered_end_point = -((H//2)+(H%2))
        self.y_filtered[filtered_start_point:filtered_end_point] = self.filtered_data[:]

        self.t_filtered = pomiar.t_measure
    
    def plots(self, *args):
        plot_options = {'signal': (self.t_signal, self.y_signal, 'b', 'Original Signal'),
                        'measure': (self.t_measure, self.y_measure, 'r.', 'Noisy Measured Signal'),
                        'filtered': (self.t_filtered, self.y_filtered, 'g--', 'Filtered Signal')}
        
        for arg in args:
            if arg in plot_options:
                t, y, marker, label = plot_options[arg]
                plt.plot(t, y, marker, label=label)
        
        plt.show()

        
signal_samples = 1000
measure_samples = 250


# pomiar = Measure(3, signal_samples, measure_samples, noise_spread=0.3)
# pomiar.filter_signal(3)
# pomiar.plots('signal', 'measure', 'filtered')

MSE_table = []

pomiar = Measure(3, signal_samples, measure_samples, noise_spread=0.5)
h_range = 13
for i in range(1, h_range*2, 2):
    print(i)
    pomiar.filter_signal(i)
    MSE_table.append(MSE(pomiar.y_signal[2::(signal_samples//measure_samples)], pomiar.y_filtered))

x = np.arange(1,h_range+1)
plt.figure()
plt.plot(x, MSE_table, marker='o', linestyle='--')
plt.show()
print(MSE_table)

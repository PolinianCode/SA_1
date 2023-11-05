from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import random

def MSE(original, data):
    N = len(original)
    sum = 0
    for i in range(0, N):
        sum += (original[i]-data[i])**2
    
    result = sum/N
    
    return result
    

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

    def filter_signal(self, H):
        self.H = H

        self.y_filtered = np.convolve(self.y_measure, np.ones(H) / H, mode='valid')

        start_index = H // 2
        end_index = start_index + len(self.y_filtered)
        self.t_filtered = pomiar.t_measure[start_index:end_index]
    
    def plots(self, *args):
        plot_options = {'signal': (self.t_signal, self.y_signal, 'b', 'Original Signal'),
                        'measure': (self.t_measure, self.y_measure, 'r.', 'Noisy Measured Signal'),
                        'filtered': (self.t_filtered, self.y_filtered, 'g--', 'Filtered Signal')}
        
        for arg in args:
            if arg in plot_options:
                t, y, marker, label = plot_options[arg]
                plt.plot(t, y, marker, label=label)
        
        plt.show()

        

pomiar = Measure(3, 1000, 250, noise_spread=0.5)

pomiar.filter_signal(7)

pomiar.plots('signal', 'measure', 'filtered')


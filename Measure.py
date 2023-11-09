import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import random


class Measure:
    def __init__(self, cycles, original_samples_number, measured_samples_number, noise_spread = 0.2):
        '''
        After initiation inside object appears:
        - Triangle symmetric signal (y = [-1;1])
        - Measured signal, which is simulation of sampling a signal with some noise/error
        '''
        self.original_t = np.linspace(0, cycles*2*np.pi, original_samples_number)
        self.original_y = signal.sawtooth(self.original_t, 0.5) 

        self.measured_t = np.linspace(0, cycles*2*np.pi, measured_samples_number) 
        self.measured_y = signal.sawtooth(self.measured_t, 0.5)

        #iterate over original signal and add some noise
        for i in range(0, len(self.measured_y)):
            #if noise_spread = 1, then standard_deviation is 0.5 in both directions
            noise = ( random.random() - 0.5 ) * noise_spread 
            self.measured_y[i] += noise

    def filter_signal(self, H):
        '''
        Simple denoise filter with moving average, where
        H (horizon) - number of averaged elements i.e. width of moving average memory
        
        Amount of filtered values must be seven less 
        '''
        self.H = H

        self.filtered_y = [None] * len(self.measured_y)
        self.filtered_array = []

        for i in range(0, len(self.measured_y)-H):
            current_average = (np.sum(self.measured_y[i:i+H]))/H
            self.filtered_array.append(current_average)

        #the only way to make filtered array comparable for further MSE calculating
        filtered_start_point = (H//2)
        filtered_end_point = -(H//2) - (H%2)
        self.filtered_y[filtered_start_point:filtered_end_point] = self.filtered_array[:]

        self.filtered_t = self.measured_t

    def plots(self, *args):
        '''
        Function for plot drawing
        '''
        plot_options = {'signal': (self.original_t, self.original_y, 'b', 'Original Signal'),
                        'measured': (self.measured_t, self.measured_y, 'r.', 'Noisy Measured Signal'),
                        'filtered': (self.filtered_t, self.filtered_y, 'g--', 'Filtered Signal')}

        for arg in args:
            if arg in plot_options:
                t, y, marker, label = plot_options[arg]
                plt.plot(t, y, marker, label=label)
                plt.legend(args)


        plt.show()
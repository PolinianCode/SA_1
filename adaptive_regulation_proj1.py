from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import random


class Sawtooth:
    def __init__(self, samples):
            self.t = np.linspace(0, 2*np.pi, samples) #time
            self.y = signal.sawtooth(self.t, 0.5) #triangle wave

class Measure:
    def __init__(self, t, y, noise_spread = 0.2):
        self.t = t
        self.y = []
        for i in y:
            noise = ( random.random() - 0.5 ) * noise_spread
            self.y.append(i + noise) 
        
fala = Sawtooth()
pomiar = Measure(fala.t, fala.y)

plt.plot(fala.t, fala.y)


plt.plot(pomiar.t, pomiar.y, '.')
plt.show()
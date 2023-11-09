from Sterowanie_adaptacyjne.SA_1.MSE import MSE
import matplotlib.pyplot as plt
import numpy as np

import Measure

def MSE_noise_variance(signal_samples, measure_samples, H):
    noise_spread_table = []
    MSE_table = []
    for i in range(0, 9):
        noise_spread = i/10
        noise_spread_table.append(noise_spread)
        pomiar = Measure(3, signal_samples, measure_samples, noise_spread)
        pomiar.filter_signal(H)
        MSE_table.append(MSE(pomiar.original_y[::(signal_samples//measure_samples)], pomiar.filtered_y))

    x = np.arange(0, 0.9, 0.1)
    plt.figure()
    plt.plot(x, MSE_table, marker='o', linestyle='--')

    plt.ylabel("MSE")
    plt.xlabel("Var(Z)")

    plt.show()
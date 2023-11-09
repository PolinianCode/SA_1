import matplotlib.pyplot as plt
import numpy as np

import MSE
import Measure


def MSE_H_plot(signal_samples, measure_samples):
    MSE_table = []

    pomiar = Measure(3, signal_samples, measure_samples, noise_spread=0.5)

    h_range = 13
    for i in range(1, h_range*2, 2):
        pomiar.filter_signal(i)
        MSE_table.append(MSE(pomiar.original_y[::(signal_samples//measure_samples)], pomiar.filtered_y))

    x = np.arange(1,(h_range)*2, 2)


    min_H = MSE_table.index(min(MSE_table)) * 2 + 1
    print(min_H)
    plt.figure()
    plt.plot(x, MSE_table, marker='o', linestyle='--')
    plt.xlabel("H")
    plt.ylabel("MSE")
    # plt.xlim(2)
    # plt.ylim(0.002, 0.01)
    plt.show()
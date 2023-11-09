import matplotlib.pyplot as plt
import numpy as np
import Measure

ORIGINAL_SAMPLES_NUM = 1000
MEASURED_SAMPLES_NUM = 250


def MSE(original, data):
    N = len(original)
    sum = 0
    for i in range(0, N):
        if data[i] is not None:
            sum += (original[i]-data[i])**2
    
    result = sum/N
    
    return result

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



MSE_noise_variance(ORIGINAL_SAMPLES_NUM, MEASURED_SAMPLES_NUM, 9)

# MSE_H_plot(signal_samples, measure_samples)

pomiar = Measure(3, ORIGINAL_SAMPLES_NUM, MEASURED_SAMPLES_NUM, noise_spread=0.3)
pomiar.filter_signal(3)
pomiar.plots('signal', 'measured', 'filtered')
pomiar.plots('signal', 'filtered')






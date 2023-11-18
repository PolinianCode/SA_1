import matplotlib.pyplot as plt
import numpy as np
import Measure

def MSE(original, data):
    N = len(original)
    sum = 0
    for i in range(0, N):
        if data[i] is not None:
            sum += (original[i]-data[i])**2

    result = sum/N

    return result


def H_plot(signal_samples, measure_samples):
    MSE_table = []

    pomiar = Measure.Measure(3, signal_samples, measure_samples, noise_spread=0.5)

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


def noise_variance_plot(signal_samples, measure_samples, H):
    MSE_table = []
    for i in range(0, 9):
        noise_spread = i/10
        pomiar = Measure.Measure(3, signal_samples, measure_samples, noise_spread)
        pomiar.filter_signal(H)
        MSE_table.append(MSE(pomiar.original_y[::(signal_samples//measure_samples)], pomiar.filtered_y))

    x = np.arange(0, 0.9, 0.1)
    plt.figure()
    plt.plot((x**2)/3, MSE_table, marker='o', linestyle='--')

    plt.ylabel("MSE")
    plt.xlabel("Var(Z)")

    plt.show()


def h_optymalne_dla_varz(signal_samples, measure_samples):

    H_opt_table = []
    VarZ_table = []

    for i in range(0, 30):
        MSE_table = []
        noise_spread = i/10
        VarZ_table.append((noise_spread ** 2) / 3)
        for j in range(1, 30):
            pomiar = Measure.Measure(3, signal_samples, measure_samples, noise_spread)
            pomiar.filter_signal(j)
            MSE_table.append(MSE(pomiar.original_y[::(signal_samples//measure_samples)], pomiar.filtered_y))

        H_opt_table.append(np.argmin(MSE_table) + 1)

    
    plt.figure()
    plt.plot(VarZ_table, H_opt_table, marker='o', linestyle='-')
    plt.ylabel("H optymalne")
    plt.xlabel("Var(Z)")

    plt.show()

    
       

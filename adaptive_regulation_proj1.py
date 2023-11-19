import measure
import MSE

ORIGINAL_SAMPLES_NUM = 1000
MEASURED_SAMPLES_NUM = 250

pomiar = measure.Measure(3, ORIGINAL_SAMPLES_NUM, MEASURED_SAMPLES_NUM, noise_spread=0.3)
pomiar.filter_signal(3)
pomiar.plots('signal', 'measured', 'filtered')
pomiar.plots('signal', 'filtered')

MSE.noise_variance_plot(ORIGINAL_SAMPLES_NUM, MEASURED_SAMPLES_NUM, 9)

MSE.H_plot(ORIGINAL_SAMPLES_NUM, MEASURED_SAMPLES_NUM)

MSE.h_optymalne_dla_varz(ORIGINAL_SAMPLES_NUM, MEASURED_SAMPLES_NUM, 100, 10, 30)







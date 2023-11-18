import Measure
import MSE

ORIGINAL_SAMPLES_NUM = 1000
MEASURED_SAMPLES_NUM = 250


MSE.noise_variance_plot(ORIGINAL_SAMPLES_NUM, MEASURED_SAMPLES_NUM, 9)

#MSE.H_plot(ORIGINAL_SAMPLES_NUM, MEASURED_SAMPLES_NUM)

pomiar = Measure.Measure(3, ORIGINAL_SAMPLES_NUM, MEASURED_SAMPLES_NUM, noise_spread=0.3)

MSE.h_optymalne_dla_varz(ORIGINAL_SAMPLES_NUM, MEASURED_SAMPLES_NUM)
#pomiar.filter_signal(3)
#pomiar.plots('signal', 'measured', 'filtered')
#pomiar.plots('signal', 'filtered')







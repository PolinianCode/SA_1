Adaptive regulation Project

This code simulates the triangle wave and it's sampling (measure) with some random noise that's Continuous uniform distributed.
After sampling, to denoise there is used a moving average filter with H (horizon) parameter. This parameter is responsible for "window size" in moving average filter:
Sample_i = (Sample_i + sample_(i+1) + ... + sample_(i+H)/H 

MSE functions draws plots with different dependencies:
1. MSE and noise variance (Var(Z))
2. MSE and H
3. H optimal and Var(Z)

from scipy.io.wavfile import read
import matplotlib.pyplot as plot
import numpy as np

#def GraphSignal()
plot.rcParams["figure.figsize"] = [7.50, 3.50]
plot.rcParams["figure.autolayout"] = True
input_wave = read("tono.wav")
signal = input_wave[1]
#plot.plot(signal[0:1024])
#plot.ylabel("Amplitude")
#plot.xlabel("Time")
#plot.show()

#def GraphPSD()
#plot.psd(signal)

noise=np.random.normal(0, 0.1, signal.shape[0])

signal_noise = signal+noise

plot.psd(noise)

#plot.plot(noise[0:1024])
#plot.ylabel("Amplitude")
#plot.xlabel("Time")
#plot.show()
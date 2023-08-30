from scipy.io.wavfile import read
import matplotlib.pyplot as plot
import numpy as np

#def GraphSignal()
##Defines Plot size
plot.rcParams["figure.figsize"] = [7.50, 3.50]
plot.rcParams["figure.autolayout"] = True

input_wave = read("tono.wav")##Opens .wav file and extracts data
signal = input_wave[1]

##Plots signal
plot.plot(signal[0:1024])
plot.ylabel("Amplitude")
plot.xlabel("Time")
plot.show()
plot.clf()

#def GraphPSD()
plot.psd(signal)##Plots Signal PSD
plot.show()
plot.clf()

#def ChannelSim
noise=np.random.normal(0, 0.1, signal.shape[0]) ##Creates Gaussian Noise with STD = 0,1

signal_noise = signal+noise ##adds noise to original signal

plot.psd(noise) ##Plots noise PSD
plot.show()
plot.clf()

plot.psd(signal_noise) ##Plots Channel PSD
plot.show()
plot.clf()

#Plots Channel Amplitude
plot.plot(signal_noise[0:1024])
plot.ylabel("Amplitude")
plot.xlabel("Time")
plot.show()
plot.clf()
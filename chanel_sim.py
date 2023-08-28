from scipy.io.wavfile import read
import matplotlib.pyplot as plot

#def GraphSignal()
plot.rcParams["figure.figsize"] = [7.50, 3.50]
plot.rcParams["figure.autolayout"] = True
input_wave = read("tono.wav")
signal = input_wave[1]
plot.plot(signal[0:1024])
plot.ylabel("Amplitude")
plot.xlabel("Time")
plot.show()

#def GraphPSD()
    
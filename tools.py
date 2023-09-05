#-------General Information-------
#Tecnol√≥gico de Costa Rica
#Escuela de Electr√≥nica
#
#Curso EL-5513 Comunicaciones El√©ctricas 1
#Prof. Laura Cabrera Quir√≥s
#
# Proyecto Programado: Sistema de modulacion y demodulaci√≥n anal√≥gico
# Etapa 1: Simulador de Ruido y Herramientas Miscel√°neas 
#
#Elaborado por:
#-Alexander Castro Lara 2017153854
#-Gabriel Hern√°ndez Calder√≥n
#-Josu√© Rojas Gonz√°lez 2017112581
#-------------------------------------------



#-------Libraries-------
import matplotlib.pyplot as plot
import numpy as np
#--------------------------

def Osciloscope(signal):
    plot.plot(signal[0:1024])
    plot.ylabel("Amplitude")
    plot.xlabel("Time")
    
def GraphPSD(signal):
    plot.psd(signal)##Plots Signal PSD
    
def FullAnalisis(signal):
    #-------Graphics windows conditioning-------
    #def GraphSignal()
    ##Defines Plot size
    plot.rcParams["figure.figsize"] = [10, 8]      # Medidas
    plot.rcParams["figure.autolayout"] = True
    #---------------------------------------------------------------------------------


    #-------Single figure for all plots-------
    #fig = plot.figure()
    #------------------------------------------------



    #-------Plots signal-------
    plot.subplot(3, 2, 1)
    plot.plot(signal[0:1024])
    plot.ylabel("Amplitude")
    plot.xlabel("Time")
    plot.title("Original Signal")
    #------------------------------



    #-------Graphic Original Signal's PSD-------
    #def GraphPSD()
    plot.subplot(3, 2, 2)
    plot.psd(signal)##Plots Signal PSD
    plot.title("PSD of Original Signal")
    #--------------------------------



    #-------Channel Simulator-------
    #def ChannelSim
    noise=np.random.normal(0, 0.1, signal.shape[0]) ##Creates Gaussian Noise with STD = 0,1

    signal_noise = signal+noise ##adds noise to original signal
    #----------------------------------------



    #-------Noise's Time Domain Plot-------
    plot.subplot(3, 2, 3)
    plot.plot(noise[0:1024])
    plot.ylabel("Amplitude")
    plot.xlabel("Time")
    plot.title("Noise in Time Domain")
    #----------------------------------------------------



    #-------Noise's PSD-------
    plot.subplot(3, 2, 4)
    plot.psd(noise) ##Plots noise PSD
    plot.title("PSD of Noise")
    #--------------------------------



    #-------Signal and Noise's PSD-------
    plot.subplot(3, 2, 6)
    plot.psd(signal_noise) ##Plots Channel PSD
    plot.title("PSD of Signal with Noise")
    #------------------------------------------------



    #-------Plots Channel Amplitude-------
    plot.subplot(3, 2, 5)
    plot.plot(signal_noise[0:1024])
    plot.ylabel("Amplitude")
    plot.xlabel("Time")
    plot.title("Signal with Noise")
    #-------------------------------------------------



    #-------Graphics Figure Conditioning-------
    plot.tight_layout()     # Adjust space

    plot.show()     # Show the figure
    #-------------------------------------------------------

    #Plots Channel Amplitude
    plot.plot(signal_noise[0:1024])
    plot.ylabel("Amplitude")
    plot.xlabel("Time")
    plot.show()
    plot.clf()
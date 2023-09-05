#-------General Information-------
#Tecnológico de Costa Rica
#Escuela de Electrónica
#
#Curso EL-5513 Comunicaciones Eléctricas 1
#Prof. Laura Cabrera Quirós
#
# Proyecto Programado: Sistema de modulacion y demodulación analógico
# Etapa 1: Simulador de Ruido y Herramientas Misceláneas 
#
#Elaborado por:
#-Alexander Castro Lara 2017153854
#-Gabriel Hernández Calderón
#-Josué Rojas González 2017112581
#-------------------------------------------



#-------Libraries-------
import numpy as np
#--------------------------



def ChannelSim(signal):
    noise=np.random.normal(0, 0.1, signal.shape[0]) ##Creates Gaussian Noise with STD = 0,1

    signal_noise = signal+noise ##adds noise to original signal
    
    return signal_noise
#-------General Information-------
#Tecnológico de Costa Rica
#Escuela de Electrónica
#
#Curso EL-5513 Comunicaciones Eléctricas 1
#Prof. Laura Cabrera Quirós
#
# Proyecto Programado: Sistema de modulación y demodulación analógico
# Etapa 1: Simulador de Ruido y Herramientas Misceláneas 
#
#Elaborado por:
#-Alexander Castro Lara 2017153854
#-Gabriel Hernández Calderón
#-Josué Rojas González 2017112581
#-------------------------------------------

#-------Libraries-------
from scipy.io.wavfile import read
import channel_sim as CS
import tools
#--------------------------

print("Options: -n (channel simulation), -a (graphs amplitude), -psd (graphs PSD) -fa (full analysis)")
print("Please type the name of your file followed by the operation you wish to execute")
print("E.g.: tono.wav -psd")
print("DO NOT SELECT MORE THAN ONE GRAPH OPTION")
selection = input("Please input operation instruction:\n")

input_file = selection.split(" ")[0]

#-------Load Audio-------
input_wave = read(input_file)##Opens .wav file and extracts data
input_signal = input_wave[1]
#------------------------------

if ("-n" in selection.split(" ")):
    input_signal = CS.ChannelSim(input_signal)
    
if ("-a" in selection.split(" ")):
    tools.Osciloscope(input_signal)

if ("-psd" in selection.split(" ")):
    tools.GraphPSD(input_signal)
    
if ("-fa" in selection.split(" ")):    
    tools.FullAnalisis(input_signal)

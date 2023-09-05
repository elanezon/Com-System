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
#-Gabriel Hern√°ndez Calder√≥n 2017238935
#-Josu√© Rojas Gonz√°lez 2017112581
#-------------------------------------------

#-------Libraries-------
from scipy.io.wavfile import read
import channel_sim as CS
#--------------------------

print("Options: -n (channel simulation), -a (graphs amplitude), -psd (graphs PSD) -fa (full analysis)")
print("Please type the name of your file followed by the operation you wish to execute")
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
    CS.Osciloscope(input_signal)

if ("-psd" in selection.split(" ")):
    CS.GraphPSD(input_signal)
    
if ("-fa" in selection.split(" ")):    
    CS.FullAnalisis(input_signal)
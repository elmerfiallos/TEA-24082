# Tendencias e Innovacion en Tecnologia Agricola (TEA)
from lib2to3.pygram import pattern_grammar
import string


horas = input("Horas trabajadas?")
valorPorHora= input ("Valor por hora?")


total  = int(horas) * int( valorPorHora)
print ("Total a pagar =" + str(total))
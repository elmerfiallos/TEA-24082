# Tendencias e Innovacion en Tecnologia Agricola (TEA)
def calcularTotal(horas, tarifa):
    horas_extras = horas - MAX_HORAS_SEM
    if(horas_extras > 0):
         total = (MAX_HORAS_SEM * tarifa) + (horas_extras * (tarifa*1.5))
    else:
       total = (horas) * (tarifa) 
    return total

try:
    MAX_HORAS_SEM= 40
    horas =int( input ("Introduzca Horas: "))
    tarifa = float (input ("Introduzca Tarifa: "))
    total = calcularTotal(horas, tarifa)
    print ("Salario: " ,total)
except: 
    print ("Error, debe de ingresar un valor numerico")
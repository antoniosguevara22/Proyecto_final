stop_words = ["es", "la", "lo","los","de","del","mi","por","con","un","una","el","unas","unos","sobre","todo",
              "también","otro","algúna","alguno","alguna","algunos","algunas","ser","soy","eres","somos","estoy","esta"
              ,"estamos","estan","como","en","calcula"]
problema= input("Escriba su problema: ")
importante=[word for word in problema.split() if word not in stop_words]

class anualidades:
    def __init__(self,pago,interes,periodo):
        self.pago= pago
        self.interes=interes
        self.periodo=periodo
        
    def vencida (self):
        V=1/(1+interes)**periodo  
        ven=pago*(1-V)/interes
        return ven
    
    def anticipada (self):
        V=1/(1+interes)**periodo  
        ant=pago*((1+interes)*(1-V)/interes)
        return ant
    
    def crecientes (self):
        V=1/(1+interes)**periodo 
        IA=pago*((((1+interes)*(1-V)/interes)-(periodo*V)))(1/interes)
        return IA

import re

separador = " "
problem=separador.join(importante)
valores=re.findall(r'\d{1,3}',problem)
datos=re.findall(r'[a-z]*',problem)

d=datos.index("pesos") , datos.index("periodos"), datos.index("tasa")

valoresdict={}
x=0
for dato in d:
    valoresdict[x] = valores[x]
    x+=1
valoresdict

pago=int(valoresdict[0])
perd=int(valoresdict[1])
interes_data=(int(valoresdict[2]))/100

data=pago, interes_data, perd

problema_fin=anualidades(data[0],data[1],data[2])

if "final" in datos:
    print(f"Su deuda seria de: {problema_fin.vencida()}")
elif "inicio"in datos :
    print(f"Su deuda seria de: {problema_fin.anticipada()}")
elif "crecientes" in datos:
    print(f"Su deuda seria de: {problema_fin.creciente()}")
else:
    print("Vaya dato perturbador: Por favor ingrese datos validos")





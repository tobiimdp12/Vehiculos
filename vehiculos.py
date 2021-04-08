def catalogar(list_class):
    for i in list_class:
        print("[",type(i).__name__,"]",i)

def catalogar_segun_cant_ruedas(list_class,ruedas_cant):
    cantidad_vehiculos=int(0)
    for i in list_class:
        if(i.ruedas==ruedas_cant):
            cantidad_vehiculos+=1
    return cantidad_vehiculos
            
class vehiculo:
    #atributos
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    #metodos
    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas )
class coche(vehiculo):
    #atributos
    def __init__(self,color,ruedas,velocidad,cilindrada):
        vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    #metodos
    def __str__(self):
        return "color {}, {} ruedas,velocidad {} km/h ,cilindrada {} cc".format(self.color, self.ruedas,self.velocidad,self.cilindrada )

class bicicleta(vehiculo):
    #atributos
    def __init__(self,color,ruedas,tipo):
        vehiculo.__init__(self,color,ruedas)
        self.tipo = tipo
    #metodos    
    def __str__(self):
        return "color {}, {} ruedas,tipo-->{}".format( self.color, self.ruedas,self.tipo)    
class camioneta(coche):
    #atributos
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        coche.__init__(self,color,ruedas,velocidad,cilindrada)
        self.carga = carga
    #metodos      
    def __str__(self):
        return "color {}, {} ruedas,velocidad {} km/h,cilindrada {} cc ,carga-->{}kg".format( self.color, self.ruedas,self.velocidad,self.cilindrada,self.carga)    

        
class motocicleta(bicicleta):
    #atributos
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        bicicleta.__init__(self,color,ruedas,tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    #metodos
    def __str__(self):
        return "color {}, {} ruedas,tipo->{},velocidad {} km/h,cilindrada {} cc".format( self.color, self.ruedas,self.tipo,self.velocidad,self.cilindrada )

auto_1=coche("rojo",4,"40","10")
auto_2=coche("rojo",4,"40","10")

bicicleta_1=bicicleta("verde",2,"urbana")
bicicleta_2=bicicleta("rosa",2,"deportiva")


camioneta_1=camioneta("violeta",6,"20000",200,10)
camioneta_2=camioneta("verde arbol",6,"20000",200,10)

motocicleta_1=motocicleta("amarillo",2,"motocross","20","2")
motocicleta_2=motocicleta("rojo",2,"ciclomotor","40","10")


list_class=[auto_1,auto_2,bicicleta_1,bicicleta_2,camioneta_1,
camioneta_2,motocicleta_1,motocicleta_2]



catalogar(list_class)
esta_bien=bool(False)
while(esta_bien==False):
    try:
        cant_ruedas=int(input("ingrese la cantidad de ruedas-->"))
        if( cant_ruedas<0):
            print("usted ingreso un numero negativo intentelo de nuevo")
            esta_bien=False
        else:
            esta_bien=True

    except:
        ValueError 
        print("usted no ingreso un numero intentelo de nuevo")
        esta_bien=False
resultados=catalogar_segun_cant_ruedas(list_class,cant_ruedas)

print("Se han encontrado {} vehículos con {} ruedas".format(resultados,cant_ruedas))
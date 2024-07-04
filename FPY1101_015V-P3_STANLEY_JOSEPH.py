import os
os.system("cls")


persona=[]

def grabarpersona():
    nombre=input("ingrese su nombre ")
    if len(nombre)==8:
        print("nombre valido")
    else:
        nombre=input("invalido ingresarlo de nuevo")    
    edad=int(input("ingrese su edad"))
    if edad >= 0:
        print("edad valido")
    else:
        print("edad no valido")
             
    nif=int(input("ingrese el numero de nif"))
    if len(nif)==13:
        print("nif valido")
    else:
        print("nif invalido")    
        
        idendificarpersona=({
            "nombre":nombre ,
            "edad":edad ,
            "nif":nif ,
        })
        
        persona.append(idendificarpersona)
        print("sus datos esta grabado exitosamente: {idendificarpersona}")
        
    
           
    
        
def buscarpersona(nif):
    for identificarpersona in persona:
        if identificarpersona["nif"]== nif:
            return persona
    
    
    
    
    
def imprimircertificados():
    precio=int(input("ingrese el precio(debes ser entre 1500 y 5000)"))
    while not 1500 < len(precio) < 5000:
        precio=input("es invalido ponerlo de nuevo")
        
    
    
    
    
    
def salir():
    print("ya saliste del programa Stanley Joseph con version SP")
    
                
while True:
    print('''
          1.-grabar persona
          2.-buscar persona
          3.-imprimir certificados
          4.-Salir''')
    try:
        op=int(input("ingrese una opcion (debes ser de 1 a 4)"))
    except:
        op=0
    #end try
    if op < 1 or op > 4:
        print("opcion ingresado no es valido")
        
    else:
        if op == 1 :
            grabarpersona()
        elif op==2 :
            buscarpersona()
        elif op==3 :
            imprimircertificados()
        else:
            salir()
            break            
    
    
            
        

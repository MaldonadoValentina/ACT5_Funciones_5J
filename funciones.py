print("Ejemplo de Funciones")
# Declarando Funciones
def hola():
    print("Alguien uso la funcion hola")

def chat(mensa):
    print(f"Chat: {mensa}")   

def ellacontesta(mensa):
    print(f"Chat ella: {mensa}")

def escribenombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")

def suma(a,b):
    r = a + b
    return r

def resta(d,e):
    rt = d - e
    return rt

def mult(j,g):
    mul = j * g
    return mul

def div(v,o):
    ds = v/o
    return ds

    # Llamadas a Funciones
hola()
chat("Que bonit@ estas")
ellacontesta("Gracias")
escribenombre("Maldonado", "Valentina")
print("1.Operacion suma")
c1 = int(input("Ingresa un numero: ")) 
c2 = int(input("Ingresa un numero: "))
damesuma = suma(c1,c2) 
print(f"─La suma de {c1} + {c2} = {damesuma}")
print("2.Operacion resta")
c3 = int(input("Ingresa un numero: ")) 
c4 = int(input("Ingresa un numero: "))
dameresta = resta(c3,c4) 
print(f"─La resta de {c3} - {c4} = {dameresta}")
print("3.Operacion multiplicación")
c5 = int(input("Ingresa un numero: ")) 
c6 = int(input("Ingresa un numero: "))
damemult = mult(c5,c6) 
print(f"─La multiplicacion de {c5} x {c6} = {damemult}")
print("4.Operacion division")
c7 = int(input("Ingresa un numero: ")) 
c8 = int(input("Ingresa un numero: "))
damedvs = div(c7,c8) 
print(f"─La division de {c7} / {c8} = {damedvs}")
print("Ejemplo de funciones")
# declarando funciones
def hola():
    print("Alguien habla la funcion")

def chat(mensa):
    print(f"Chat {mensa}")

def ellacontesta(mensa):
    print(f"Chat {mensa}")

def escribrenombre(ap,n):
    print(f"Tu nombre completo es :{n} {ap}")

def suma(a,b):
    s=a+b
    return s   
##llamadas a funciones
hola()
chat("Que bonita estas")
ellacontesta("gracias")
escribrenombre("Gaytan", "Roberto")


def resta(a,b):
    r=a-b
    return r
def mult(a,b):
    m=a*b
    return m 
def div(a,b):
    d=a/b
    return d

print("Operaciones basicas")
c1=int(input("Ingresa un numero "))
c2=int(input("Ingresa un numero "))
damesuma=suma(c1,c2)
print (f"La SUMA DE {c1}+{c2}={damesuma}")

print("-- RESTA --")
c3=int(input("Ingresa un numero "))
c4=int(input("Ingresa un numero "))
dameresta=resta(c3,c4)
print (f"La RESTA DE {c3}-{c4}={dameresta}")

print("-- DIVISION --")
c5=int(input("Ingresa un numero "))
c6=int(input("Ingresa un numero "))
damediv=div(c5,c6)
print (f"La RESTA DE {c5}/{c6}={damediv}")

print("-- MULTIPLICACION --")
c7=int(input("Ingresa un numero "))
c8=int(input("Ingresa un numero "))
damemult=mult(c7,c8)
print (f"La RESTA DE {c7}x{c8}={damemult}")
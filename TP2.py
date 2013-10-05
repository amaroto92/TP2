print("        Lenguaje de Programacion PROLOG")

global BaseConocimientos
BaseConocimientos=[]


global Lexico
Lexico = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',',','.','(',')','[',']']


#### Menu de Inicio ####################################################################
def MenuInicio():
	print("Menu de opciones:")
	print("1) Modo Administrativo")
	print("2) Modo Consulta")
	print
	opcion=input("Cual opcion desea hacer? : ")
	print
	if opcion==1:
	    print 
	    return MenuAdministrativo()
	elif opcion==2:
	    print 
	    print ("CONSULTAS NO ESTA HECHO TODAVIA")
	    return MenuInicio()
	else:
	    print ("Valor ingresado es invalido, por favor elija una opcion")
	    print 
	    return MenuInicio()

#### Menu Administrativo ####################################################################
def MenuAdministrativo():
	print ("Modo Administrativo")
	print("1) Ingresar un nuevo hecho")
	print("2) Ingresar una nueva regla")
	print("3) Mostrar Base de Conocimientos")
	print("4) Regresar a Menu Principal")
	opcion=input("Que desea hacer? : ")
	if opcion==1:
	    return IngresarHecho()
	elif opcion==2:
	    return IngresarRegla()
	elif opcion==3:
	    return MostrarBaseConocimiento()
	elif opcion==4:
	    return MenuInicio()
	else:
	    print ("Valor ingresado es invalido, por favor elija una opcion")
	    print 
	    return MenuAdministrativo()

#### Ingresar Hechos ####################################################################   
def IngresarHecho():
	print
	print("      Ingresar Hechos")
	print("*Un hecho debe terminar con un punto(.) al final")
	print("*Un hecho puede tener 0 a N argumentos")
	print("Ejemplo:  perro(bruno).      amigo(daniel,felipe).")
	print
	return IngresarHecho_Aux()

def IngresarHecho_Aux():
	hecho=raw_input(": ")
	ScannerHecho(hecho)
	BaseConocimientos.append(hecho)
	opcion=input("hecho ingresado, 1 para agregar nuevo hecho, 2 para volver al menu: ")
	if opcion==1:
	    return IngresarHecho_Aux()
	else:
	    print
	    return MenuAdministrativo()

def ScannerHecho(hecho):
	for caracter in hecho:
		if caracter in Lexico:
			True
		else:
			print("Error de scanner: "+caracter+" no es token valido")
			return
    
    

#### Ingresar Regla ###################################################################  
def IngresarRegla():
	print("Ingresar Regla")


#### Mostrar Hechos ###################################################################
def MostrarBaseConocimiento():
	print
	print("       Base de Conocimientos")
	print
	for i in range(0,len(BaseConocimientos)):
	    print(BaseConocimientos[i])
	print
	return MenuAdministrativo()

#### Consultas #########################################################################   
def Consultas():
	print("Consultas")



MenuInicio()

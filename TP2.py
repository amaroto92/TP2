print(" Lenguaje de Programacion PROLOG")

global BaseConocimientos
BaseConocimientos=['nl','fail','write(args)'] #Lista que contiene la BC y le agregamos los built-in predicates.


global Lexico
Lexico = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',',','.','(',')','[',']','-',':','_']


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
		print ("Valor ingresado es invalido, por favor elija 			una opcion")
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
	print("Ingresar Hechos")
	print("*Un hecho debe terminar con un punto(.) al final")
	print("*Un hecho puede tener 0 a N argumentos")
	print("Ejemplo: perro(bruno). amigo(daniel,felipe).")
	print
	return IngresarHecho_Aux()

def IngresarHecho_Aux():
	hecho=raw_input(": ")
	if ScannerHecho(hecho) and ParserHecho(hecho): #Si pasa las etapas de Scanner y Parser correctamente, agrega el hecho a la BC.

		BaseConocimientos.append(hecho) #append lo agrega al final de 							la lista.
		print("Hecho ingresado")
		opcion=input("hecho ingresado, presione 1 para agregar nuevo hecho y 2 para volver al menu: ")
		if opcion==1:
			return IngresarHecho_Aux()
		else:
			print
			return MenuAdministrativo()
	else:
		print("Error al ingresar hecho a la Base de Conocimiento") 
		#No se agrega nada.
		opcion=input("presione 1 para agregar nuevo hecho y 2 para volver al menu: ")
		if opcion==1:
			return IngresarHecho_Aux()
		else:
			print
			return MenuAdministrativo()

# Funcion para validar el lexico del hecho:		

def ScannerHecho(hecho):
	for caracter in hecho:
		if caracter.lower() in Lexico[:-2]:
			True
		else:
			print("Error de scanner: "+caracter+" no es token 				valido")
			return False
	return True
	
# Funcion para validar la sintaxis del hecho :   

def ParserHecho(hecho):
	
	banderaparentisis = False
	if hecho[-1] != '.': #Que termine con punto.
		print("Un hecho tiene que terminar con punto")
		return False
	else:
	
		for i in range(0,len(hecho)):
		
			print (hecho[i])

			if i==0 and (hecho[i].islower() == False): # Que 				empieze con minuscula.
				print("Un hecho tiene que empezar con Minuscula")
				return False
		
			elif hecho[i] == '(' :
				banderaparentisis = True #Bandera para saber 					que tiene parentesis, este se tiene que cerrar 					y tiene que haber un alfa numerico despues del 					parentesis abierto.
				if hecho[i+1].isalnum() == False:
					print("Error despues del ( ")
					return False
				elif banderaparentisis == True:
					if hecho[-2] !=')':
						print("No se cerro parentesis")
						return False

			elif hecho[i] == ',':
				if hecho[i+1].isalnum() ==False:
				#Despues de una coma tiene que haber un alfa 					numerico.
					print("Error despues de la ,")
					return False
			
		return True #Paso todas las pruebas del Parser correctamente.

			 
				
		
			

#### Ingresar Regla ###################################################################
def IngresarRegla():
	print
	print(" Ingresar Reglas")
	print("*Una Regla debe terminar con un punto(.) al final")
	print("*Una Regla puede tener 0 a N argumentos")
	print("*Toda Regla puede tener N antecedentes")
	print("Ejemplo: amigo(daniel,felipe).")
	print
	return IngresarRegla_Aux()

def IngresarRegla_Aux():
	regla=raw_input(": ")
	if ScannerRegla(regla) and ParserRegla(regla): #Si pasa las etapas de Scanner y Parser correctamente, agrega el hecho a la BC.

		BaseConocimientos.append(regla) #append lo agrega al final de 							la lista.
		print("Regla ingresado")
		opcion=input("Regla ingresada, presione 1 para agregar nueva regla y 2 para volver al menu: ")
		if opcion==1:
			return IngresarRegla_Aux()
		else:
			print
			return MenuAdministrativo()
	else:
		print("Error al ingresar regla a la Base de Conocimiento") 
		#No se agrega nada.
		opcion=input("presione 1 para agregar nueva regla y 2 para volver al menu: ")
		if opcion==1:
			return IngresarRegla_Aux()
		else:
			print
			return MenuAdministrativo()
		

# Funcion para validar el lexico de la regla
def ScannerRegla(regla):
	
	for caracter in regla:
		if caracter.lower() in Lexico:
			True
		else:
			print("Error de scanner: "+caracter+" no es token valido")
			return False
	return True

# Funcion para validar la sintaxis de la regla

def ParserRegla(regla):

# FALTA!!



#### Mostrar Hechos ###################################################################
def MostrarBaseConocimiento():
	print
	print("Base de Conocimientos")
	print
	for i in range(0,len(BaseConocimientos)):
		print(BaseConocimientos[i])
	print
	return MenuAdministrativo()

#### Consultas #########################################################################
def Consultas():
	print("Consultas")



MenuInicio()

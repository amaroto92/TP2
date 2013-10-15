print(" Lenguaje de Programacion PROLOG")

global BaseConocimientos
BaseConocimientos=['nl','fail','write(args)'] #Lista que contiene la BC y le agregamos los built-in predicates.


global Lexico
Lexico = ['_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',',','.','(',')','[',']','-',':']

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
		print 
		return Consultas()
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

#Funcion para validar el lexico del hecho:
#Devuelve true si los caracteres de hecho se encuentran en la lista lexico y False si encuentra 1 que no.
		
def ScannerHecho(hecho):
	for caracter in hecho:
		if caracter.lower() in Lexico[:-2]:
			True
		else:
			print("Error de scanner: "+caracter+" no es token valido")
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
		
			#print (hecho[i])

			if i==0 and (hecho[i].islower() == False): # Que empieze con minuscula.
				print("Un hecho tiene que empezar con Minuscula")
				return False
		
			elif hecho[i] == '(' :
				banderaparentisis = True #Bandera para saber que tiene parentesis, este se tiene que cerrar 					y tiene que haber un alfa numerico despues del parentesis abierto.
				if ((hecho[i+1].isalnum() == False) and (hecho[i+1] != "_")):
					print("Error despues del ( ")
					return False
				elif banderaparentisis == True:
					if hecho[-2] !=')':
						print("No se cerro parentesis")
						return False

			elif hecho[i] == ',':
				if ((hecho[i+1].isalnum() == False) and (hecho[i+1] != "_")):
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
	print("Ejemplo: animal(X):-perro(X),estavivo(X).")
	print
	return IngresarRegla_Aux()

def IngresarRegla_Aux():
	regla=raw_input(": ")
	if ScannerRegla(regla) and ParserRegla(regla) and VerificarAridad(regla): #Si pasa las etapas de Scanner y Parser correctamente, agrega el hecho a la BC.

		BaseConocimientos.append(regla) #append lo agrega al final de 							la lista.
		print("Regla ingresada")
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
	
	banderadospuntos = False
	
	if regla[-1] != '.': #Verificamos que termine con punto.
		print("Una regla tiene que terminar con punto")
		return False
	
	else:
		regla = regla[:-1] #le quitamos el punto del final a la regla.
		
		for i in range(0,len(regla)):
			
		
			if regla[i] == ':':
				banderadospuntos=True
				cuerporegla=remplaza2(remplaza(regla[i+2:],0).split(","))  #En una lista cuerporegla vamos a tener todos los hechos del cuerpo en una lista, los hechos se encuentran separados por `,` ; con esto se separaran para agregarlos a la lista
				
				#print (regla[:i]+'.')
				if ParserHecho(regla[:i]+'.') and regla[i+1]=="-": #Chequeamos que el encabezado de la regla sea un hecho valido y que despues de los : haya un -


					 True
				else:
					return False
		if banderadospuntos==False:
			print("No tiene los dos puntos :" )
			return False
		else:

			for hecho in cuerporegla: #Ciclo para recorrer la lista que contiene el cuerpo de la regla.

				#print("Hecho +. "+ hecho +" .")
				if ParserHecho(hecho+".") == False: #Verificamos que cada hecho que esta en el cuerpo sea un hecho valido.
					return False
			return True	

			
##Funcion para remplezar las "," que separan los argumentos dentro de los parentesis de cada hecho, esto con el fin de utilizar el '.split' de forma mas sencilla##

def remplaza(string1,P0):
    largo=len(string1)
    P1=0
    P2=0
    if P0>=largo: #condicion de parada, si la posicion inicial es mayor o igual que el largo
        return (string1) #retorna el string con puntos dentro del parentesis en vez de comas.
    else:
        if P0<largo-1: #comprobar que la posicion inicial sea menor que el largo.
            for i in range (P0,largo): #ciclo que busca el primer parentesis
                if string1[i]=='(':
                    P1=i # y le asigna a p1 la posicion del parentesis
                   
                    break
		elif (i==largo-1):
			return remplaza(string1,largo)
        if P1+1<=largo-1: #comprobar que haya un parentesis de cierre.
            for f in range (P1+1,largo):
                if string1[f]==')': # si lo encuentra
                    P2=f+1 #le asigna la posicion a P2.
		
            
                    return remplaza((string1[:P1]+(string1[P1:P2].replace(",","."))+string1[P2:]),P2) # envia lo que esta antes del parentesis, lo que esta dentro remplaza las , por . y envia lo que esta despues del parentesis. Y como segundo parametro envia la nueva posicion inicial despues de que se cierre el parentesis.

##Funcion que auxiliar de 'remplaza', esta cambiara los simbolos que en 'remplaza' fueron cambiados, por los simbolos que deben de ser##

def remplaza2(lista):
	lista_retorno=[]
	for hecho in lista:
		lista_retorno.append(hecho.replace(".",","))
	return lista_retorno
       
#### Verificar aridad de funciones que tienen el mismo nombre ######

def VerificarAridad(regla):
	encabezadobase = ""
	encabezadoregla = ""
	particionregla=""
	particionbase=""

	for caracter in range(0,len(regla)):
		if regla[caracter] == ':':
			encabezadoregla = regla[:caracter]
			particionregla = encabezadoregla.partition("(") #Separa el string en la primera ocurrencia del parametro, y retorna una tupla de 3 elementos: la parte antes del separador, el separador mismo, y lo que esta despues del separador.

			

	
	for i in range(0,len(BaseConocimientos)):
		particionbase =  BaseConocimientos[i].partition("(") #Separa el string en la primera ocurrencia del parametro, y retorna una tupla de 3 elementos: la parte antes del separador, el separador mismo, y lo que esta despues del separador.

		
		if BaseConocimientos[i] == regla:
			print ("Regla ya existe en la Base")
			return False
		elif particionbase[0] == particionregla[0]:
			subparticionregla=particionregla[2].partition(")")
			subparticionbase=particionbase[2].partition(")")
			if len(subparticionbase[0]) == len(subparticionregla[0]):
				print ("Regla ya existe con la misma aridad")
				return False
	
	return True




#### Mostrar Hechos y Reglas ###################################################################
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

	consulta= raw_input("?-")

	if BuscarUnificacion(HacerLista(consulta))==True:

		print("YES")

	else:

		print("NO")

	return Consultas()



def HacerLista(consulta):

	ListaConsulta=[]

	for i in range(0,len(consulta)): 

		if consulta[i] == '(' : 

			functor = consulta[:i]

			predicado= consulta[i+1:-2]

	parametros=predicado.split(",")

	ListaConsulta+=[functor]

	ListaConsulta+=[parametros]

	return ListaConsulta



def BuscarUnificacion(Consulta):

	bandera=0 ## cero si es NO y 1 si va a ser YES	

	for i in range(0,len(BaseConocimientos)):

		if EsRegla(BaseConocimientos[i])!=True:

			#print("es hecho lo q esta en BC")

			if bandera==0 or bandera==1: ###

				Conocimiento=HacerLista(BaseConocimientos[i])

				if Consulta[0]==Conocimiento[0] and len(Consulta[1])==len(Conocimiento[1]):

					resultado=UnificacionArgumentos(Consulta[1],Conocimiento[1],len(Consulta[1]))

					if resultado==1:

						return True

					elif resultado==2:

						bandera=1

					else:

						bandera=0

				##else:

					##bandera=-1  ## por si los functores no son iguales

		else:

			#print("es una regla lo q esta en BC")

			regla=BaseConocimientos[i]

			#print(regla)

			for j in range(0,len(regla)):

				if (regla[j] == ':') and (regla[j+1] == '-'): 

					parametros = regla[j+2:] #Los parametros de predicado

					ListaRegla= HacerLista(regla[:j]+".") #Functor con argumento en HacerLista

			#print( parametros)

			#print(ListaRegla)

			if ListaRegla[0]==Consulta[0] and len(Consulta[1])==len(ListaRegla[1]):

				###hay q unificar los parametros de la regla

				parametroslista = parametros.split('),') #Parametros separados en lista para revisar uno por uno

				for k in range(0,len(parametroslista)-1):

					parametroslista[k]+=")."

				for l in range(0,len(parametroslista)):

					#print(parametroslista[l])

					if BuscarUnificacion(HacerLista(parametroslista[l])) == False:

						return False

				return True

	if bandera==0:

		return False

	elif bandera==1:

		return True







def EsRegla(Consulta):

	for i in range(0, len(Consulta)):

		if Consulta[i] == ':' and Consulta[i+1] == '-':

			return True

	return False



##

def EsBuiltIn(Consulta):

	if Consulta=="nl":

		print

		return True

	elif Consulta=="fail":

		return False

	##else



def UnificacionArgumentos(argsconsulta, argshecho, cant_args):

	bandera=0

	bandera2=""

	n = 0 

	while (n<=((cant_args)-1)): ## las dos son variables para reglas

		if esvariable(argsconsulta[n]) == False and esvariable(argshecho[n]) == True:

			argshecho[n] = argsconsulta[n]

			n+=1 

		elif esvariable(argsconsulta[n]) == False and esvariable(argshecho[n]) == False:

			if argsconsulta[n] == argshecho[n]:

				n+=1

				bandera=1

			else:	

				return 0

		elif esvariable(argsconsulta[n]) == True and esvariable(argshecho[n])== False:

			bandera2=argsconsulta[n]+" = "+argshecho[n]

			n+=1

	if bandera2!="":

		comando=raw_input(bandera2)

		if comando==";":

			bandera=2

		elif comando=="":

			bandera=1

		else:

			##error

			bandera=1

	return bandera



def esvariable(dato):

	if dato.islower() == True:

		return False 

	else: 

		return True

			

				





MenuInicio()

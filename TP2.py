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
		print("ingrese: menu  para regresar al menu principal")
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
	consulta= raw_input("?-") #recibe una consulta
	if consulta.lower()=="menu": #verifica si desea volver al menu
		print
		return MenuInicio() #si ingresa menu, las consultas se detienen y se regresa al menu principal
	elif BuscarUnificacion(HacerLista(consulta))==True: #transforma la consulta en modo Lista y la trata de unificar
		print("YES") # si hubo unificacion total, se imprime YES
	else:
		print("NO") # de lo contrario se imprime NO
	return Consultas() # al dar el resultado de una consulta (Yes, No) se reinicia para otra nueva consulta

def HacerLista(consulta): #Funcion que transforma en lista una consulta: A(B) -> [A,[b1,b2,b3]]
	if EsBuiltIn(consulta)==4: # primero verifica que la consulta no es un built in function. 4 significa que no lo es.
		ListaConsulta=[] 
		for i in range(0,len(consulta)): # se recorre la consulta para separar lo que este antes de los parentesis.
			if consulta[i] == '(' : 
				functor = consulta[:i]
				predicado= consulta[i+1:-2]
		parametros=predicado.split(",") # se separan los parametros del predicado.
		ListaConsulta+=[functor]
		ListaConsulta+=[parametros] # y se ingresan en la lista.
		return ListaConsulta
	else:
		return consulta

def BuscarUnificacion(Consulta): #Funcion que trata de unificar las consultas.
	bandera=0 # utilizamos una bandera, 0 para retornar NO y 1 para retornar YES al final de la unificacion.
	for i in range(0,len(BaseConocimientos)): # se recorre toda la Base de Conocimientos para unificar con todas las posibles.
		if EsBuiltIn(BaseConocimientos[i])!=4: # si la BC muestra un BuiltIn, la trata de unificar.
			BuiltIn=EsBuiltIn(BaseConocimientos[i])
			if BuiltIn==1 and Consulta=="nl": # si unifica con nl, imprime una linea vacia.
				print
				bandera=1
			elif BuiltIn==2 and Consulta=="fail": # si unifica con fail, termina de unificar y continua con la BC.
				return False
			elif BuiltIn==3 and Consulta[:6]=="write(": # verifica si es write.
				Escribir=Consulta[6:-1]
				if EsVariable(Escribir)==False: # si lo que esta dentro del write es constante, la escribe.
					print(Escribir)
					bandera=1
		elif EsRegla(BaseConocimientos[i])!=True and EsBuiltIn(BaseConocimientos[i])==4: # trata de unificar con Hechos.
			Conocimiento=HacerLista(BaseConocimientos[i])
			if Consulta[0]==Conocimiento[0] and len(Consulta[1])==len(Conocimiento[1]): # si el functor y la cantidad de parametros son iguales, trata de unificar todos los parametros..
				resultado=UnificacionArgumentos(Consulta[1],Conocimiento[1],len(Consulta[1]))
				if resultado==1: # si la unificacion de parametros retorna 1, es que fue correcto y retorna YES.
					return True
				elif resultado==2: # si es 2, significa que se pidio backtracking con ;.
					bandera=1
				else:
					bandera=0 # cero si no unifico.
		elif EsRegla(BaseConocimientos[i])==True and EsBuiltIn(BaseConocimientos[i])==4: # Trata de unificar con reglas de la BC.
			regla=BaseConocimientos[i]
			for j in range(0,len(regla)): # separa el predicado de la regla.
				if (regla[j] == ':') and (regla[j+1] == '-'): 
					parametros = regla[j+2:] #Los parametros de predicado
					ListaRegla= HacerLista(regla[:j]+".") #Functor con argumento en HacerLista
			if ListaRegla[0]==Consulta[0] and len(Consulta[1])==len(ListaRegla[1]): # si la regla y la cantidad de argumentos son iguales, trata de unificar el predicado.
				###hay q unificar los parametros de la regla###############################################################
				parametroslista = parametros[:-2].split('),') #Parametros separados en lista para revisar uno por uno
				for k in range(0,len(parametroslista)): # revisamos q builtIns sean considerados como parametros.
					if parametroslista[k][:3]=="nl,": # para ln, ya que no debe tener parentesis.
						parametroslista[k]+=")."
						parametroslista=parametroslista[:k]+['nl']+[parametroslista[k][3:]]
					elif parametroslista[k][:5]=="fail,": # para fail, ya que no debe tener parentesis.
						parametroslista[k]+=")."
						parametroslista=parametroslista[:k]+['fail']+[parametroslista[k][5:]]
					elif parametroslista[k][:2]=="_,": # para los unbound, ya que solo debe ser un guion bajo.
						parametroslista[k]+=")."
						parametroslista=parametroslista[:k]+['_']+[parametroslista[k][5:]]			
					elif parametroslista[k][:6]=="write(": #para los write, ya que no termina con punto.
						parametroslista[k]+=")"
					else:
						parametroslista[k]+=")."
				for l in range(0,len(parametroslista)): # recorremos los parametros y unificamos.
					if parametroslista[l]!="_": # si no es unbound, debe tratar la unificacion.
						if BuscarUnificacion(HacerLista(parametroslista[l])) == False: # si no unifica algun parametro, este retorna falso.
							return False
					else:
						True # si es unbound, unifica de una vez.
				return True
	if bandera==0: # si el resultado final de la bandera es cero, imprime NO en consola.
		return False
	elif bandera==1: # imprime YES de lo contrario.
		return True

def EsRegla(Consulta): #Funcion para verificar si es regla.
	for i in range(0, len(Consulta)): # recorre lo consultado para verificar si contiene un :-
		if Consulta[i] == ':' and Consulta[i+1] == '-':
			return True # si los contiene, es regla.
	return False # de lo contrario, es un hecho.

def EsBuiltIn(Consulta): #Funcion para verificar si es Built In Function.
	if Consulta=="nl": 
		return 1
	elif Consulta=="fail":
		return 2
	elif Consulta[:6]=="write(" and Consulta[-1]==")":
		return 3
	else:
		return 4

def UnificacionArgumentos(argsconsulta, argshecho, cant_args): #Funcion para unificar los parametros.
	bandera=0 #utilizamos esta bandera para retornarla y saber valor de unificacion.
	ValorVariable="" #utilizamos esta variable para guardar el valor del backtracking.
	n = 0 
	while (n<=((cant_args)-1)): #recorremos todos los parametros unificandolos.
		if argsconsulta[n]=="_": # si el parametro es unbound, unifica.
			n+=1
		elif EsVariable(argsconsulta[n]) == False and EsVariable(argshecho[n]) == True: # si la consulta es una constante, y la BC es una Variable, unifica.
			argshecho[n] = argsconsulta[n]
			n+=1 
		elif EsVariable(argsconsulta[n]) == False and EsVariable(argshecho[n]) == False: # si la consulta es un hecho, y la BC es un constante, unifica.
			if argsconsulta[n] == argshecho[n]:
				n+=1
				bandera=1 #indica que si  unifico.
			else:	
				return 0
		elif EsVariable(argsconsulta[n]) == True and EsVariable(argshecho[n])== False: # si la consulta es una variable, y la BC es una constante, unifica.
			ValorVariable=argsconsulta[n]+" = "+argshecho[n] # anotamos cual es el valor para backtracking.
			n+=1
	if ValorVariable!="": #Verificamos si hay valor para hacer backtracking.
		comando=raw_input(ValorVariable) # imprimimos valor, y se pide ; si se desea backtracking.
		if comando==";":
			bandera=2 # 2 para indicar que si se desea backtracking.
		elif comando=="":
			bandera=1 # 1 si solo desea continuar con la siguiente consulta.
		else:
			bandera=1
	return bandera # se retorna el valor de la unificacion de los parametros.

def EsVariable(dato): #Funcion para indicar si un dato es variable o constante.
	if dato.islower() == True: #si todo es minuscula, es constante.
		return False 
	else: 
		return True
			
			

MenuInicio()

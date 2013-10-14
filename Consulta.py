+global BaseConocimientos
+BaseConocimientos=['perro(ruffo).','perro(ruffo,theo).','perro(theo,theo).','perro(theo).','grande(ruffo).','perro_grande(X):-perro(ruffo),grande(X).'] #Lista que contiene la BC y le agregamos los built-in predicates.
+
+def Inicio():
+	consulta= raw_input(":::::")
+	if BuscarUnificacion(HacerLista(consulta))==True:
+		print("YES")
+	else:
+		print("NO")
+	return Inicio()
+
+def HacerLista(consulta):
+	ListaConsulta=[]
+	for i in range(0,len(consulta)): 
+		if consulta[i] == '(' : 
+			functor = consulta[:i]
+			predicado= consulta[i+1:-2]
+	parametros=predicado.split(",")
+	ListaConsulta+=[functor]
+	ListaConsulta+=[parametros]
+	return ListaConsulta
+
+def BuscarUnificacion(Consulta):
+	for i in range(0,len(BaseConocimientos)):
+		if EsRegla(BaseConocimientos[i])!=True:
+			bandera=0
+			for x in range(0,len(BaseConocimientos)):
+				if bandera==0 or bandera==1:
+					Conocimiento=HacerLista(BaseConocimientos[x])
+					if Consulta[0]==Conocimiento[0] and len(Consulta[1])==len(Conocimiento[1]):
+						resultado=UnificacionArgumentos(Consulta[1],Conocimiento[1],len(Consulta[1]))
+						if resultado==1:
+							return True
+						elif resultado==2:
+							bandera=1
+						else:
+							bandera=0
+					##else:
+						##bandera=-1  ## por si los functores no son iguales
+			if bandera==0:
+				return False
+			elif bandera==1 or bandera==2:
+				return True
+		else:
+			print("si es regla")
+			regla=BaseConocimientos[i]
+			for j in range(0,len(regla)):
+				if (regla[j] == ':') and (regla[j+1] == '-'): 
+					parametros = regla[j+2:]
+					ListaRegla= HacerLista(regla[:j]+".")
+					return
+			print( parametros)
+			print(ListaRegla)
+			if ListaRegla[0]==Consulta[0] and len(Consulta[1])==len(ListaRegla[1]):
+				###hay q unificar los parametros de la regla
+				parametroslista = parametros.split('),')
+				for k in range(0,len(parametroslista)-1):
+					parametroslista[k]+=")."
+				print (parametroslista)
+				for l in range(0,len(parametroslista)):
+					print(parametroslista[l])
+					if BuscarUnificacion(HacerLista(parametroslista[l])) == False:
+						return False
+				return True
+	return False
+
+
+
+def EsRegla(Consulta):
+	for i in range(0, len(Consulta)):
+		if Consulta[i] == ':' and Consulta[i+1] == '-':
+			return True
+	return False
+
+##
+def EsBuiltIn(Consulta):
+	if Consulta=="nl":
+		print
+		return True
+	elif Consulta=="fail":
+		return False
+	##else
+
+def UnificacionArgumentos(argsconsulta, argshecho, cant_args):
+	bandera=0
+	bandera2=""
+	n = 0 
+	while (n<=((cant_args)-1)):
+		if esvariable(argsconsulta[n]) == False and esvariable(argshecho[n]) == True:
+			argshecho[n] = argsconsulta[n]
+			n+=1 
+		elif esvariable(argsconsulta[n]) == False and esvariable(argshecho[n]) == False:
+			if argsconsulta[n] == argshecho[n]:
+				n+=1
+				bandera=1
+			else:	
+				return 0
+		elif esvariable(argsconsulta[n]) == True and esvariable(argshecho[n])== False:
+			bandera2=argsconsulta[n]+" = "+argshecho[n]
+			n+=1
+	if bandera2!="":
+		comando=raw_input(bandera2)
+		if comando==";":
+			bandera=2
+		elif comando=="":
+			bandera=1
+		else:
+			bandera=1
+	return bandera
+
+def esvariable(dato):
+	if dato.islower() == True:
+		return False 
+	else: 
+		return True
+			
+				
+
+Inicio()
+

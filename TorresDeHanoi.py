def torresHanoi(discos,torre1,torre2,torre3):
	#Caso base
	if(discos==1):
		return print("Mover disco de torre "+str(torre1)+" a torre "+str(torre3))
	else:
		#discos-1,origen,destino,auxiliar
		torresHanoi(discos-1,torre1,torre3,torre2)
		print("Mover disco de torre "+str(torre1)+" a torre "+str(torre3))
		torresHanoi(discos-1,torre2,torre1,torre3)

torresHanoi(4,"A","B","C")

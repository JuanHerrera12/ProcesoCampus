archivo = open("/home/spukN01-020/Desktop/ProcesoCampus-1/Archivos/salas.txt", "w")

archivo.write("sputnik\n\t")
archivo.write("apolo\n")


archivo.writelines(["houston\n", "artemis"])


archivo.close()
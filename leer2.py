import consulta_TFG2
import subprocess


def leer_archivo(db, id):
    # Using readlines()
    file1 = open('gcode.txt', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
        if "C12" in line:
            C12 = line.split()
            number = C12[1]
            print(number)
            consulta_TFG2.set(db,id, number)
        if "S12" in line:
            S12 = line.split()
            imagen = S12[1]
            tiempo = S12[2]
            print("La imagen {} tiene que estar {} segundos en pantalla".format(imagen, tiempo))
            #subprocess.call(["gcc", "fbtest1.c"])
            #tmp=subprocess.call("./fbtest1")
            #temp = subprocess.call('sh ./ejecucion')
            subprocess.run(["sh ./ejecucion.sh", imagen, tiempo])
            #print(temp)
            estado = consulta_TFG2.consulta_estado(db, id)
            print("El estado actual es :")
            print(estado+1)
            consulta_TFG2.actualiza_estado(db, id)

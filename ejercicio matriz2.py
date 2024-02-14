
def main():
    nombres_alumnos = []
    nombres_materias = []
    for i in range(100):
        nombre_alumno = input("Ingrese el nombre del alumno {}: ".format(i + 1))
        nombres_alumnos.append(nombre_alumno)
    for i in range(6):
        nombre_materia = input("Ingrese el nombre de la materia {}: ".format(i + 1))
        nombres_materias.append(nombre_materia)
    calificaciones = []
    for alumno in range(100):
        calificaciones_alumno = []
        for materia in range(6):
            calificacion = float(input("Calificación de {} para {}: ".format(nombres_alumnos[alumno], nombres_materias[materia])))
            calificaciones_alumno.append(calificacion)
        calificaciones.append(calificaciones_alumno)

    calificaciones_transpuestas = [[calificaciones[j][i] for j in range(100)] for i in range(6)]

    while True:
        alumno = int(input("Ingrese el número de alumno (1-100) o -1 para salir: "))
        if alumno == -1:
            print("¡Hasta luego!")
            break
        if alumno < 1 or alumno > 100:
            print("Número de alumno inválido.")
            continue
        materia = int(input("Ingrese el número de materia (1-6) o -1 para salir: "))
        if materia == -1:
            print("¡Hasta luego!")
            break
        if materia < 1 or materia > 6:
            print("Número de materia inválido.")
            continue
        calificacion = calificaciones_transpuestas[materia - 1][alumno - 1]
        print("La calificación del alumno {} en la materia {} es: {}".format(nombres_alumnos[alumno - 1], nombres_materias[materia - 1], calificacion))

if __name__ == "__main__":
    main()

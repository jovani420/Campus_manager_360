class Persona:
    def __init__(self, nombre, apellido_p, apellido_m, edad):
        self.__nombre = nombre
        self.__apellido_p = apellido_p
        self.__apellido_m = apellido_m
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @property
    def apellido_p(self):
        return self.__apellido_p
    @apellido_p.setter
    def apellido_p(self, apellido_p):
        self.__apellido_p = apellido_p

    @property
    def apellido_m(self):
        return self.__apellido_m

    @apellido_m.setter
    def apellido_m(self, apellido_m):
        self.__apellido_m = apellido_m

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, apellido_p, apellido_m, edad, promedio, expediente):
        Persona.__init__(self, nombre, apellido_p, apellido_m, edad)
        self.__promedio = promedio
        self.__expediente = expediente

    @property
    def promedio(self):
        return self.__promedio
    @promedio.setter
    def promedio(self, promedio):
        self.__promedio = promedio

    @property
    def expediente(self):
        return self.__expediente
    @expediente.setter
    def expediente(self, expediente):
        self.__expediente = expediente


class Profesor(Persona):
    def __init__(self, nombre, apellido_p, apellido_m, edad, num_empleado):
        Persona.__init__(self, nombre, apellido_p, apellido_m, edad)
        self.__num_empleado = num_empleado

    @property
    def num_empleado(self):
        return self.num_empleado
    @num_empleado.setter
    def num_empleado(self, num_empleado):
        self.__num_empleado = num_empleado

class Investigador(Persona):
    def __init__(self, nombre, apellido_p, apellido_m, edad, publicaciones):
        Persona.__init__(self, nombre, apellido_p, apellido_m, edad)
        self.__publicaciones = publicaciones
    @property
    def publicaciones(self):
        return self.__publicaciones
    @publicaciones.setter
    def publicaciones(self, publicaciones):
        self.__publicaciones = publicaciones

class ProfesorInvestigacion(Profesor, Investigador):
    def __init__(self, nombre, apellido_p, apellido_m, edad, num_empleado, publicaciones):
        Profesor.__init__(self, nombre, apellido_p, apellido_m, edad, num_empleado)
        Investigador.__init__(self, nombre, apellido_p, apellido_m, edad, publicaciones)

class ControlAcademico:
    lista_estudiante = []
    lista_profesor_investigador = []

    def registrar_estudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido_p = input("Ingrese el apellido paterno del estudiante: ")
        apellido_a = input("Ingrese el apellido materno del estudiante: ")
        edad =  int(input("Ingrese la edad del estudiante: "))
        promedio = float(input("Ingrese la promedio del estudiante: "))
        expediente = input("Ingrese la expediente del estudiante: ")

        estudiante = Estudiante(nombre, apellido_p, apellido_a, edad, promedio, expediente)

        self.lista_estudiante.append(estudiante)

        print("\n El estudiante registrado correctamente \n")
    def mostrar_estudiante(self):
        for i, estudiante in enumerate(self.lista_estudiante, start=1):
            print("Nombre: ", estudiante.nombre)
            print("Apellido Paterno: ", estudiante.apellido_p)
            print("Apellido Materno: ", estudiante.apellido_m)
            print("Edad: ", estudiante.edad)
            print("Promedio: ", estudiante.promedio)
            print("Expediente: ", estudiante.expediente)
            print("\n")
    def actualizar_estudiante(self):
        expediente = input("Ingrese la expediente del estudiante: ")
        for i, estudiante in enumerate(self.lista_estudiante):
            if expediente == estudiante.expediente:
                print("Nombre: ", estudiante.nombre)
                print("Apellido Paterno: ", estudiante.apellido_p)
                print("Apellido Materno: ", estudiante.apellido_m)
                print("Edad: ", estudiante.edad)
                print("Promedio: ", estudiante.promedio)

                print("\n El estudiante actualizado correctamente \n")
            else:
                print("No se encontro extudiante")
    def registrar_profesor_investigador(self):
        nombre = input("Ingrese eel nombre profesor investigador: ")
        apellido_p = input("Ingrese el apellido paterno profesor investigador: ")
        apellido_m = input("Ingrese el apellido materno profesor investigador: ")
        edad = int(input("Ingrese la edad profesor investigador: "))
        num_empleado = float(input("Ingrese el numero empleado del profesor investigador: "))
        expediente = input("Ingrese el expediente profesor investigador: ")

        profesor_investigador = ProfesorInvestigacion(nombre, apellido_p, apellido_m, edad, num_empleado, expediente)

        self.lista_estudiante.append(profesor_investigador)

        print("\n El Profesor investigador registrado correctamente \n")
    def mostrar_profesor_investigador(self):
        for i, profesor_investigador in enumerate(self.lista_profesor_investigador):
            print("Nombre: ", profesor_investigador.nombre)
            print("Apellido Paterno: ", profesor_investigador.apellido_p)
            print("Apellido Materno: ", profesor_investigador.apellido_m)
            print("Edad: ", profesor_investigador.edad)
            print("Promedio: ", profesor_investigador.num_empleado)
            print("Expediente: ", profesor_investigador.expediente)
    def actualizar_profesor_investigador(self):
        num_empleado = input("Ingrese el numero de empleado: ")
        for i, profesor_investigador in enumerate(self.lista_profesor_investigador):
            if num_empleado == profesor_investigador.num_empleado:
                nombre = input("Ingrese el nombre del profesor investigador: ")
                apellido_p = input("Ingrese el apellido paterno investigador: ")
                apellido_m = input("Ingrese el apellido materno investigador: ")
                edad = int(input("Ingrese la edad investigador: "))
                promedio = float(input("Ingrese la promedio investigador: "))
                expediente = input("Ingrese el expediente investigador: ")

                profesor_investigador = ProfesorInvestigacion(nombre, apellido_p, apellido_m, edad, promedio, expediente)

                self.lista_profesor_investigador.append(profesor_investigador)

                print("\n El Profesor investigador se actualizo correctamente \n")

    def menu(self):
        while True:
            print("[1]. Registrar Estudiante")
            print("[2]. Mostrar Estudiantes")
            print("[3]. Actualizar Estudiante")
            print("[4]. Registrar Profesor Investigador")
            print("[5]. Mostrar Profesores Investigadores")
            print("[6]. Actualizar Profesor Investigador")
            opcion = int(input("Ingrese la opcion del menu: "))
            if opcion == 1:
                self.registrar_estudiante()
            if opcion == 2:
                self.mostrar_profesor_investigador()
            if opcion == 3:
                self.actualizar_profesor_investigador()
            if opcion == 4:
                self.registrar_profesor_investigador()
            if opcion == 5:
                self.mostrar_profesor_investigador()
            if opcion == 6:
                self.actualizar_profesor_investigador()


control_academico = ControlAcademico()
control_academico.menu()










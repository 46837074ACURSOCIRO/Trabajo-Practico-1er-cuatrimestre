class EstudianteNoEncontrado(Exception):
    pass


class CursoNoEncontrado(Exception):
    pass


class CursoLleno(Exception):
    pass


class EstudianteDuplicado(Exception):
    pass


class CursoDuplicado(Exception):
    pass


class YaInscripto(Exception):
    pass


class NoInscripto(Exception):
    pass


class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera
        self.cursos = []


class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad = capacidad
        self.estudiantes = []


class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []

    def buscar_estudiante(self, matricula):
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                return estudiante
        raise EstudianteNoEncontrado()

    def buscar_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        raise CursoNoEncontrado()

    def agregar_estudiante(self):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        matricula = input("Matricula: ")
        carrera = input("Carrera: ")

        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                raise EstudianteDuplicado()

        self.estudiantes.append(Estudiante(nombre, apellido, matricula, carrera))
        print("Estudiante agregado")

    def agregar_curso(self):
        nombre = input("Nombre del curso: ")
        codigo = input("Codigo: ")
        profesor = input("Profesor: ")
        capacidad = int(input("Capacidad: "))

        for curso in self.cursos:
            if curso.codigo == codigo:
                raise CursoDuplicado()

        self.cursos.append(Curso(nombre, codigo, profesor, capacidad))
        print("Curso agregado")

    def inscribir(self):
        matricula = input("Matricula del estudiante: ")
        codigo = input("Codigo del curso: ")

        estudiante = self.buscar_estudiante(matricula)
        curso = self.buscar_curso(codigo)

        for curso_estudiante in estudiante.cursos:
            if curso_estudiante.codigo == codigo:
                raise YaInscripto()

        if len(curso.estudiantes) >= curso.capacidad:
            raise CursoLleno()

        estudiante.cursos.append(curso)
        curso.estudiantes.append(estudiante)
        print("Estudiante inscripto")

    def dar_baja(self):
        matricula = input("Matricula del estudiante: ")
        codigo = input("Codigo del curso: ")

        estudiante = self.buscar_estudiante(matricula)
        curso = self.buscar_curso(codigo)

        if curso not in estudiante.cursos:
            raise NoInscripto()

        estudiante.cursos.remove(curso)
        curso.estudiantes.remove(estudiante)
        print("Estudiante dado de baja")

    def mostrar_cursos(self):
        if len(self.cursos) == 0:
            print("No hay cursos")

        for curso in self.cursos:
            print(curso.nombre, curso.codigo, "Profesor:", curso.profesor)
            print("Inscriptos:", len(curso.estudiantes), "/", curso.capacidad)

    def mostrar_estudiantes(self):
        if len(self.estudiantes) == 0:
            print("No hay estudiantes")

        for estudiante in self.estudiantes:
            print(estudiante.nombre, estudiante.apellido, "Matricula:", estudiante.matricula)
            print("Carrera:", estudiante.carrera)

            for curso in estudiante.cursos:
                print("Curso:", curso.nombre)


def main():
    facultad = Facultad()

    while True:
        print("\n1 Agregar estudiante")
        print("2 Agregar curso")
        print("3 Inscribir estudiante")
        print("4 Dar de baja")
        print("5 Ver cursos")
        print("6 Ver estudiantes")
        print("0 Salir")

        opcion = input("Opcion: ")

        try:
            if opcion == "1":
                facultad.agregar_estudiante()
            elif opcion == "2":
                facultad.agregar_curso()
            elif opcion == "3":
                facultad.inscribir()
            elif opcion == "4":
                facultad.dar_baja()
            elif opcion == "5":
                facultad.mostrar_cursos()
            elif opcion == "6":
                facultad.mostrar_estudiantes()
            elif opcion == "0":
                break
            else:
                print("Opcion incorrecta")

        except EstudianteNoEncontrado:
            print("No se encontro el estudiante")
        except CursoNoEncontrado:
            print("No se encontro el curso")
        except CursoLleno:
            print("El curso esta lleno")
        except EstudianteDuplicado:
            print("Ese estudiante ya existe")
        except CursoDuplicado:
            print("Ese curso ya existe")
        except YaInscripto:
            print("El estudiante ya esta inscripto")
        except NoInscripto:
            print("El estudiante no esta inscripto en ese curso")
        except ValueError:
            print("La capacidad tiene que ser un numero")


main()
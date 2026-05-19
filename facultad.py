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

    def inscribir_en_curso(self, curso):
        self.cursos.append(curso)

    def dar_baja_curso(self, curso):
        self.cursos.remove(curso)

    def mostrar(self):
        if not self.cursos:
            cursos_str = "ninguno"
        else:
            nombres = [c.nombre for c in self.cursos]
            cursos_str = ", ".join(nombres)
        return f"  {self.nombre} {self.apellido} (Mat: {self.matricula}) - {self.carrera} -> Cursos: {cursos_str}"


class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad = capacidad
        self.estudiantes = []

    def hay_cupo(self):
        return len(self.estudiantes) < self.capacidad

    def inscribir_estudiante(self, estudiante):
        if not self.hay_cupo():
            raise CursoLleno()
        self.estudiantes.append(estudiante)

    def desinscribir_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)

    def cupos_disponibles(self):
        return self.capacidad - len(self.estudiantes)

    def mostrar(self):
        return f"  {self.nombre} (Cód: {self.codigo}) - Prof: {self.profesor} -> Inscriptos: {len(self.estudiantes)}/{self.capacidad}"


class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []

    def buscar_estudiante(self, matricula):
        for e in self.estudiantes:
            if e.matricula == matricula:
                return e
        raise EstudianteNoEncontrado()

    def buscar_curso(self, codigo):
        for c in self.cursos:
            if c.codigo == codigo:
                return c
        raise CursoNoEncontrado()

    def agregar_estudiante(self, nombre, apellido, matricula, carrera):
        try:
            self.buscar_estudiante(matricula)
            raise EstudianteDuplicado()
        except EstudianteNoEncontrado:
            pass
        self.estudiantes.append(Estudiante(nombre, apellido, matricula, carrera))
        print(f"\nEstudiante {nombre} {apellido} registrado.")

    def agregar_curso(self, nombre, codigo, profesor, capacidad):
        try:
            self.buscar_curso(codigo)
            raise CursoDuplicado()
        except CursoNoEncontrado:
            pass
        self.cursos.append(Curso(nombre, codigo, profesor, capacidad))
        print(f"\nCurso {nombre} agregado.")

    inscribir_estudiante = None
    inscribir_en_curso = None

    def inscribir(self, matricula, codigo):
        estudiante = self.buscar_estudiante(matricula)
        curso = self.buscar_curso(codigo)

        for c in estudiante.cursos:
            if c.codigo == codigo:
                raise YaInscripto()

        curso.inscribir_estudiante(estudiante)
        estudiante.inscribir_en_curso(curso)
        print(f"\n{estudiante.nombre} se inscribió en {curso.nombre}.")

    def dar_baja(self, matricula, codigo):
        estudiante = self.buscar_estudiante(matricula)
        curso = self.buscar_curso(codigo)

        esta_inscripto = False
        for c in estudiante.cursos:
            if c.codigo == codigo:
                esta_inscripto = True
                break

        if not esta_inscripto:
            raise NoInscripto()

        curso.desinscribir_estudiante(estudiante)
        estudiante.dar_baja_curso(curso)
        print(f"\n{estudiante.nombre} se dio de baja de {curso.nombre}.")

    def ver_cursos(self):
        print("\nCursos:")
        if not self.cursos:
            print("  No hay cursos cargados.")
        else:
            for curso in self.cursos:
                print(curso.mostrar())

    def ver_estudiantes(self):
        print("\nEstudiantes:")
        if not self.estudiantes:
            print("  No hay estudiantes registrados.")
        else:
            for estudiante in self.estudiantes:
                print(estudiante.mostrar())


def pedir(mensaje):
    valor = input(mensaje).strip()
    if not valor:
        raise ValueError("No puede estar vacío.")
    return valor


def main():
    facu = Facultad()
    print("Sistema de Gestión de la Facultad")

    while True:
        print("\nOpciones:")
        print("  1. Registrar estudiante")
        print("  2. Agregar curso")
        print("  3. Inscribir estudiante a curso")
        print("  4. Dar baja de curso")
        print("  5. Ver cursos")
        print("  6. Ver estudiantes")
        print("  0. Salir")

        try:
            op = input("\nElegí: ").strip()

            if op == "0":
                print("\nChau!\n")
                break

            elif op == "1":
                print("\nRegistrar estudiante")
                nombre = pedir("Nombre: ")
                apellido = pedir("Apellido: ")
                matricula = pedir("Número de matrícula: ")
                carrera = pedir("Carrera: ")
                facu.agregar_estudiante(nombre, apellido, matricula, carrera)

            elif op == "2":
                print("\nAgregar curso")
                nombre = pedir("Nombre del curso: ")
                codigo = pedir("Código del curso: ")
                profesor = pedir("Profesor: ")
                capacidad = int(pedir("Capacidad máxima: "))
                facu.agregar_curso(nombre, codigo, profesor, capacidad)

            elif op == "3":
                print("\nInscribir a curso")
                matricula = pedir("Matrícula del estudiante: ")
                codigo = pedir("Código del curso: ")
                facu.inscribir(matricula, codigo)

            elif op == "4":
                print("\nDar baja de curso")
                matricula = pedir("Matrícula del estudiante: ")
                codigo = pedir("Código del curso: ")
                facu.dar_baja(matricula, codigo)

            elif op == "5":
                facu.ver_cursos()

            elif op == "6":
                facu.ver_estudiantes()

            else:
                print("\nOpción inválida.")

        except (EstudianteNoEncontrado, CursoNoEncontrado, CursoLleno,
                EstudianteDuplicado, CursoDuplicado, YaInscripto, NoInscripto) as e:
            print(f"\nError: {type(e).__name__}")

        except ValueError as e:
            print(f"\n{e}")

        input("\nEnter para seguir...")


if __name__ == "__main__":
    main()
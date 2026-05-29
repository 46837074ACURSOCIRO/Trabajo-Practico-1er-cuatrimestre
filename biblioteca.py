class LibroNoEncontrado(Exception):
    pass


class MiembroNoEncontrado(Exception):
    pass


class LibroNoDisponible(Exception):
    pass


class LibroNoPrestado(Exception):
    pass


class LibroDuplicado(Exception):
    pass


class MiembroDuplicado(Exception):
    pass


class DevolucionNoAutorizada(Exception):
    pass


class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False
        self.dni_miembro = ""


class Miembro:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.libros = []


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        raise LibroNoEncontrado()

    def buscar_miembro(self, dni):
        for miembro in self.miembros:
            if miembro.dni == dni:
                return miembro
        raise MiembroNoEncontrado()

    def agregar_libro(self):
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")

        for libro in self.libros:
            if libro.isbn == isbn:
                raise LibroDuplicado()

        self.libros.append(Libro(titulo, autor, isbn))
        print("Libro agregado")

    def agregar_miembro(self):
        nombre = input("Nombre: ")
        dni = input("DNI: ")

        for miembro in self.miembros:
            if miembro.dni == dni:
                raise MiembroDuplicado()

        self.miembros.append(Miembro(nombre, dni))
        print("Miembro agregado")

    def prestar_libro(self):
        dni = input("DNI del miembro: ")
        isbn = input("ISBN del libro: ")

        miembro = self.buscar_miembro(dni)
        libro = self.buscar_libro(isbn)

        if libro.prestado:
            raise LibroNoDisponible()

        libro.prestado = True
        libro.dni_miembro = dni
        miembro.libros.append(libro)
        print("Libro prestado")

    def devolver_libro(self):
        dni = input("DNI del miembro: ")
        isbn = input("ISBN del libro: ")

        miembro = self.buscar_miembro(dni)
        libro = self.buscar_libro(isbn)

        if not libro.prestado:
            raise LibroNoPrestado()

        if libro.dni_miembro != dni:
            raise DevolucionNoAutorizada()

        libro.prestado = False
        libro.dni_miembro = ""
        miembro.libros.remove(libro)
        print("Libro devuelto")

    def mostrar_libros(self):
        if len(self.libros) == 0:
            print("No hay libros")

        for libro in self.libros:
            if libro.prestado:
                print(libro.titulo, "- prestado")
            else:
                print(libro.titulo, "- disponible")

    def mostrar_miembros(self):
        if len(self.miembros) == 0:
            print("No hay miembros")

        for miembro in self.miembros:
            print(miembro.nombre, miembro.dni)
            for libro in miembro.libros:
                print("Tiene:", libro.titulo)


def main():
    biblioteca = Biblioteca()

    while True:
        print("\n1 Agregar miembro")
        print("2 Agregar libro")
        print("3 Prestar libro")
        print("4 Devolver libro")
        print("5 Ver libros")
        print("6 Ver miembros")
        print("0 Salir")

        opcion = input("Opcion: ")

        try:
            if opcion == "1":
                biblioteca.agregar_miembro()
            elif opcion == "2":
                biblioteca.agregar_libro()
            elif opcion == "3":
                biblioteca.prestar_libro()
            elif opcion == "4":
                biblioteca.devolver_libro()
            elif opcion == "5":
                biblioteca.mostrar_libros()
            elif opcion == "6":
                biblioteca.mostrar_miembros()
            elif opcion == "0":
                break
            else:
                print("Opcion incorrecta")

        except LibroNoEncontrado:
            print("No se encontro el libro")
        except MiembroNoEncontrado:
            print("No se encontro el miembro")
        except LibroNoDisponible:
            print("El libro no esta disponible")
        except LibroNoPrestado:
            print("El libro no estaba prestado")
        except LibroDuplicado:
            print("Ese libro ya existe")
        except MiembroDuplicado:
            print("Ese miembro ya existe")
        except DevolucionNoAutorizada:
            print("Ese miembro no puede devolver ese libro")


main()
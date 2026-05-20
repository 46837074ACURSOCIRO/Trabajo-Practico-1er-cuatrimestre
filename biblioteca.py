class LibroNoEncontrado(Exception):
    pass

class LibroNoDisponible(Exception):
    pass

class LibroNoPrestado(Exception):
    pass

class MiembroNoEncontrado(Exception):
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
        self.prestado_a = None

    def mostrar(self):
        if self.prestado:
            return f"  {self.titulo} de {self.autor} (ISBN: {self.isbn}) -> prestado a {self.prestado_a.nombre}"
        return f"  {self.titulo} de {self.autor} (ISBN: {self.isbn}) -> disponible"


class Miembro:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.libros_prestados = []

    def agregar_libro(self, libro):
        self.libros_prestados.append(libro)

    def quitar_libro(self, libro):
        self.libros_prestados.remove(libro)

    def mostrar(self):
        if not self.libros_prestados:
            return f"  {self.nombre} (DNI: {self.dni}) -> tiene: ningún libro"
        nombres = []
        for l in self.libros_prestados:
            nombres.append(f"'{l.titulo}'")
        return f"  {self.nombre} (DNI: {self.dni}) -> tiene: {', '.join(nombres)}"


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

    def agregar_libro(self, titulo, autor, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                raise LibroDuplicado()
        self.libros.append(Libro(titulo, autor, isbn))
        print(f"Agregué '{titulo}' al catálogo.")

    def agregar_miembro(self, nombre, dni):
        for miembro in self.miembros:
            if miembro.dni == dni:
                raise MiembroDuplicado()
        self.miembros.append(Miembro(nombre, dni))
        print(f"Listo, {nombre} ya esta registrado/a.")

    def prestar_libro(self, dni, isbn):
        miembro = self.buscar_miembro(dni)
        libro = self.buscar_libro(isbn)
        if libro.prestado:
            raise LibroNoDisponible()
        libro.prestado = True
        libro.prestado_a = miembro
        miembro.agregar_libro(libro)
        print(f"Listo Le preste '{libro.titulo}' a {miembro.nombre}.")

    def devolver_libro(self, dni, isbn):
        miembro = self.buscar_miembro(dni)
        libro = self.buscar_libro(isbn)
        if not libro.prestado:
            raise LibroNoPrestado()
        if libro.prestado_a != miembro:
            raise DevolucionNoAutorizada()
        libro.prestado = False
        libro.prestado_a = None
        miembro.quitar_libro(libro)
        print(f"\nGracias! {miembro.nombre} devolvió '{libro.titulo}'.")

    def ver_libros(self):
        print("\nLibros en la biblioteca:")
        if not self.libros:
            print("  Todavía no hay libros cargados.")
        else:
            for libro in self.libros:
                print(libro.mostrar())

    def ver_miembros(self):
        print("\nMiembros registrados:")
        if not self.miembros:
            print("  Todavía no hay miembros registrados.")
        else:
            for miembro in self.miembros:
                print(miembro.mostrar())


def pedir_dato(mensaje):
    valor = input(mensaje).strip()
    if not valor:
        raise ValueError("No podés dejar esto vacío.")
    return valor


def main():
    biblio = Biblioteca()
    print("Bienvenido a la biblioteca!")

    while True:
        print("\nQué querés hacer?")
        print("  1. Registrar miembro")
        print("  2. Agregar libro")
        print("  3. Prestar libro")
        print("  4. Devolver libro")
        print("  5. Ver libros")
        print("  6. Ver miembros")
        print("  0. Salir")

        try:
            opcion = input("\nElegí una opción: ").strip()

            if opcion == "0":
                print("\nChau, que tengas buen día!\n")
                break

            elif opcion == "1":
                print("\nRegistrar miembro")
                nombre = pedir_dato("Nombre: ")
                dni = pedir_dato("DNI: ")
                biblio.agregar_miembro(nombre, dni)

            elif opcion == "2":
                print("\nAgregar libro")
                titulo = pedir_dato("Título: ")
                autor = pedir_dato("Autor: ")
                isbn = pedir_dato("ISBN: ")
                biblio.agregar_libro(titulo, autor, isbn)

            elif opcion == "3":
                print("\nPrestar libro")
                dni = pedir_dato("DNI: ")
                isbn = pedir_dato("ISBN: ")
                biblio.prestar_libro(dni, isbn)

            elif opcion == "4":
                print("\nDevolver libro")
                dni = pedir_dato("DNI: ")
                isbn = pedir_dato("ISBN: ")
                biblio.devolver_libro(dni, isbn)

            elif opcion == "5":
                biblio.ver_libros()

            elif opcion == "6":
                biblio.ver_miembros()

            else:
                print("Esa opción no existe.")

        except (LibroNoEncontrado, LibroNoDisponible, LibroNoPrestado,
                MiembroNoEncontrado, LibroDuplicado, MiembroDuplicado,
                DevolucionNoAutorizada) as e:
            print(f"\nError: {type(e).__name__}")

        except ValueError as e:
            print(f"\n{e}")

        input("\nEnter para seguir...")


if __name__ == "__main__":
    main()
=======
class Biblioteca:
    def __init__ (self):
        self.Miembros=[]
        self.Libros=[]
    def agregarMiembro(self, nombre, dni):
        miembro = Miembros(nombre, dni)
        self.Miembros.append(miembro)
    def prestarlibro (self, dni,isbn):
        # recorrer lista libros hasta que q coincida con el isbn
        for l in self.Libros:
            if l.ISBN == isbn:
                if l.estaDisponible():
                    l.prestarLibros()
                    l.regitrarLibroPrestado(l.Isbn)

class Libros:
    def __init__ (self,titulo, autor , ISBN):
        self.titulo =titulo
        self.autor =autor
        self.estadoprestado = False
        self.ISBN =ISBN

class Miembros:
    def __init__ (self,nombre , dni):
        self.nombre =nombre
        self.dni =dni
        self.librosPrestados=[]


def main ():
    biblioteca= Biblioteca()
    while True:

        print("0- Salir")
        print("1- Agregar Miembro")
        print("2- Agregar Libro")
        print("3- Prestar Libro")
        print("4- Devolver Libro")
        print("5- Consultar Estado del Libro")
        print("6- Consultar estado de miembro")  

        opcion = input("Ingrese una opcion")


        if opcion == "1":
            nombre = input("Ingrese el nombre del miembro: ")
            dni = input("Ingrese el dni del miembro: ")
            biblioteca.agregarMiembro(nombre, dni)
            
        elif opcion =="3":
            dni = input("Ingrese el dni del miembro: ")
            isbn= input("Ingrese el isbn del libro: ")
            biblioteca.prestarlibro(dni,isbn)
>>>>>>> 3dcd943f360fb60e8bbdd6495f20a7c780bc4903
